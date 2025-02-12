import tempfile
import subprocess
import gzip
import os
import urllib.request
from argparse import ArgumentParser
import sys

def append_ercc(gtf_file, fasta_file):
    ercc_fa = ERCC_BUCKET + "ERCC92.fasta.gz"
    with tempfile.NamedTemporaryFile(delete=True, suffix=".gz") as tmp_fa:
        urllib.request.urlretrieve(ercc_fa, tmp_fa.name)
        with open(fasta_file, 'ab') as f_out, gzip.open(tmp_fa.name, 'rb') as f_in:
            f_out.write(f_in.read())

    ercc_gtf = ERCC_BUCKET + "ERCC92.gtf.gz"
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