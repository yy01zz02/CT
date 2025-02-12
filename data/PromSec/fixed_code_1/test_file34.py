import json
from io import BytesIO
import logging
import os

import attr
from six import text_type
from twisted.internet import address
import twisted.logger
from twisted.web.http_headers import Headers
from twisted.web.server import Request, Site
from twisted.web.http import unquote
from twisted.test.proto_helpers import MemoryReactorClock
from OpenSSL import crypto

from sydent.sydent import Sydent, parse_config_dict


FAKE_SERVER_CERT_PEM = """
-----BEGIN CERTIFICATE-----
MIIDlzCCAn+gAwIBAgIUC8tnJVZ8Cawh5tqr7PCAOfvyGTYwDQYJKoZIhvcNAQEL
BQAwWzELMAkGA1UEBhMCQVUxEzARBgNVBAgMClNvbWUtU3RhdGUxITAfBgNVBAoM
GEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZDEUMBIGA1UEAwwLZmFrZS5zZXJ2ZXIw
HhcNMjAwMTE0MTc1MzQwWhcNMzAwMTExMTc1MzQwWjBbMQswCQYDVQQGEwJBVTET
MBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50ZXJuZXQgV2lkZ2l0cyBQ
dHkgTHRkMRQwEgYDVQQDDAtmYWtlLnNlcnZlcjCCASIwDQYJKoZIhvcNAQEBBQAD
ggEPADCCAQoCggEBANNzY7YHBLm4uj52ojQc/dfQCoR+63IgjxZ6QdnThhIlOYgE
3y0Ks49bt3GKmAweOFRRKfDhJRKCYfqZTYudMcdsQg696s2HhiTY0SpqO0soXwW4
6kEIxnTy2TqkPjWlsWgGTtbVnKc5pnLs7MaQwLIQfxirqD2znn+9r68WMOJRlzkv
VmrXDXjxKPANJJ9b0PiGrL2SF4QcF3zHk8Tjf24OGRX4JTNwiGraU/VN9rrqSHug
CLWcfZ1mvcav3scvtGfgm4kxcw8K6heiQAc3QAMWIrdWhiunaWpQYgw7euS8lZ/O
C7HZ7YbdoldknWdK8o7HJZmxUP9yW9Pqa3n8p9UCAwEAAaNTMFEwHQYDVR0OBBYE
FHwfTq0Mdk9YKqjyfdYm4v9zRP8nMB8GA1UdIwQYMBaAFHwfTq0Mdk9YKqjyfdYm
4v9zRP8nMA8GA1UdEwEB/wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAEPVM5/+
Sj9P/CvNG7F2PxlDQC1/+aVl6ARAz/bZmm7yJnWEleBSwwFLerEQU6KFrgjA243L
qgY6Qf2EYUn1O9jroDg/IumlcQU1H4DXZ03YLKS2bXFGj630Piao547/l4/PaKOP
wSvwDcJlBatKfwjMVl3Al/EcAgUJL8eVosnqHDSINdBuFEc8Kw4LnDSFoTEIx19i
c+DKmtnJNI68wNydLJ3lhSaj4pmsX4PsRqsRzw+jgkPXIG1oGlUDMO3k7UwxfYKR
XkU5mFYkohPTgxv5oYGq2FCOPixkbov7geCEvEUs8m8c8MAm4ErBUzemOAj8KVhE
tWVEpHfT+G7AjA8=
-----END CERTIFICATE-----
"""


def make_sydent(test_config={}):
    if 'db' not in test_config:
        test_config['db'] = {'db.file': ':memory:'}
    else:
        test_config['db'].setdefault('db.file', ':memory:')

    reactor = MemoryReactorClock()
    return Sydent(reactor=reactor, cfg=parse_config_dict(test_config))


@attr.s
class FakeChannel(object):
    site = attr.ib(type=Site)
    _reactor = attr.ib()
    result = attr.ib(default=attr.Factory(dict))
    _producer = None

    @property
    def json_body(self):
        if not self.result:
            raise Exception("No result yet.")
        return json.loads(self.result["body"].decode("utf8"))

    @property
    def code(self):
        if not self.result:
            raise Exception("No result yet.")
        return int(self.result["code"])

    @property
    def headers(self):
        if not self.result:
            raise Exception("No result yet.")
        h = Headers()
        for i in self.result["headers"]:
            h.addRawHeader(*i)
        return h

    def writeHeaders(self, version, code, reason, headers):
        self.result["version"] = version
        self.result["code"] = code
        self.result["reason"] = reason
        self.result["headers"] = headers

    def write(self, content):
        if not isinstance(content, bytes):
            raise ValueError("Should be bytes! " + repr(content))

        if "body" not in self.result:
            self.result["body"] = b""

        self.result["body"] += content

    def registerProducer(self, producer, streaming):
        self._producer = producer
        self.producerStreaming = streaming

        def _produce():
            if self._producer:
                self._producer.resumeProducing()
                self._reactor.callLater(0.1, _produce)

        if not streaming:
            self._reactor.callLater(0.0, _produce)

    def unregisterProducer(self):
        if self._producer is None:
            return

        self._producer = None

    def requestDone(self, _self):
        self.result["done"] = True

    def getPeer(self):
        return address.IPv4Address("TCP", "127.0.0.1", 3423)

    def getHost(self):
        return None

    @property
    def transport(self):
        return self

    def getPeerCertificate(self):
        return crypto.load_certificate(crypto.FILETYPE_PEM, FAKE_SERVER_CERT_PEM)


class FakeSite:
    pass


def make_request(
    reactor,
    method,
    path,
    content=b"",
    access_token=None,
    request=Request,
    shorthand=True,
    federation_auth_origin=None,
):
    if not isinstance(method, bytes):
        method = method.encode("ascii")

    if not isinstance(path, bytes):
        path = path.encode("ascii")

    if (
        shorthand
        and not path.startswith(b"/_matrix")
    ):
        path = b"/_matrix/identity/v2/" + path
        path = path.replace(b"//", b"/")

    if not path.startswith(b"/"):
        path = b"/" + path

    if isinstance(content, dict):
        content = json.dumps(content)
    if isinstance(content, text_type):
        content = content.encode("utf8")

    site = FakeSite()
    channel = FakeChannel(site, reactor)

    req = request(channel)
    req.process = lambda: b""
    req.content = BytesIO(content)
    req.postpath = list(map(unquote, path[1:].split(b"/")))

    if access_token:
        req.requestHeaders.addRawHeader(
            b"Authorization", b"Bearer " + access_token.encode("ascii")
        )

    if federation_auth_origin is not None:
        req.requestHeaders.addRawHeader(
            b"Authorization",
            b"X-Matrix origin=%s,key=,sig=" % (federation_auth_origin,),
        )

    if content:
        req.requestHeaders.addRawHeader(b"Content-Type", b"application/json")

    req.requestReceived(method, path, b"1.1")

    return req, channel


class ToTwistedHandler(logging.Handler):
    tx_log = twisted.logger.Logger()

    def emit(self, record):
        log_entry = self.format(record)
        log_level = record.levelname.lower().replace("warning", "warn")
        self.tx_log.emit(
            twisted.logger.LogLevel.levelWithName(log_level), "{entry}", entry=log_entry
        )


def setup_logging():
    root_logger = logging.getLogger()

    log_format = (
        "%(asctime)s - %(name)s - %(lineno)d - %(levelname)s"
        " - %(message)s"
    )

    handler = ToTwistedHandler()
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)

    log_level = os.environ.get("SYDENT_TEST_LOG_LEVEL", "ERROR")
    root_logger.setLevel(log_level)


setup_logging()
