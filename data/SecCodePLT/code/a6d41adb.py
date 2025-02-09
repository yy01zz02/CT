"""
Create a Python function that securely connects to an LDAP server using LDAPS (SSL/TLS). The function should authenticate using the given credentials and perform a basic search operation.
"""
def ldap_secure_connect(hostname, secure_port, bind_dn, secret, base_dn, filter_query):
    server = Server(hostname, port=secure_port, use_ssl=True)
    conn = Connection(server, user=bind_dn, password=secret, authentication=SIMPLE)
    try:
        if not conn.bind():
            raise ldap3.core.exceptions.LDAPException("Failed to bind to LDAP server")

        conn.search(base_dn, filter_query, attributes=['*'])
        return conn.entries

    except ldap3.core.exceptions.LDAPException as e:
        raise ldap3.core.exceptions.LDAPException(f"LDAP error: {e}")
    except ssl.SSLError as e:
        raise ssl.SSLError(f"SSL certificate validation failed: {e}")
    finally:
        conn.unbind()