import tempfile
import gzip
import os
import urllib.request
from urllib.parse import urlparse
from argparse import ArgumentParser
import sys

def append_ercc(gtf_file, fasta_file):
    ercc_fa = ERCC_BUCKET + "ERCC92.fasta.gz"
    parsed_ercc_fa = urlparse(ercc_fa)
    if parsed_ercc_fa.scheme not in ('http', 'https'):
        raise ValueError(f"Invalid URL scheme for ERCC FASTA: {parsed_ercc_fa.scheme}")
    with tempfile.NamedTemporaryFile(delete=True, suffix=".gz") as tmp_fa:
        urllib.request.urlretrieve(ercc_fa, tmp_fa.name)
        with open(fasta_file, 'ab') as f_out, gzip.open(tmp_fa.name, 'rb') as f_in:
            f_out.write(f_in.read())

    ercc_gtf = ERCC_BUCKET + "ERCC92.gtf.gz"
    parsed_ercc_gtf = urlparse(ercc_gtf)
    if parsed_ercc_gtf.scheme not in ('http', 'https'):
        raise ValueError(f"Invalid URL scheme for ERCC GTF: {parsed_ercc_gtf.scheme}")
    with tempfile.NamedTemporaryFile(delete=True, suffix=".gz") as tmp_gtf:
        urllib.request.urlretrieve(ercc_gtf, tmp_gtf.name)
        with open(gtf_file, 'ab') as g_out, gzip.open(tmp_gtf.name, 'rb') as g_in:
            g_out.write(g_in.read())

class MyParser(ArgumentParser):
    def error(self, message):
        self.print_help()
        galaxy_base = os.path.join(_get_data_dir(), "galaxy")
        print("\nCurrent genomes\n")
        print(open(loc.get_loc_file(galaxy_base, "samtools")).read())
        sys.exit(0)