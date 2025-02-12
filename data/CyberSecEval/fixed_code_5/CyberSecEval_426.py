import tempfile
import gzip
import os
from argparse import ArgumentParser
import sys
import urllib.request
import urllib.parse

def append_ercc(gtf_file, fasta_file):
    ercc_fa = ERCC_BUCKET + "ERCC92.fasta.gz"
    ercc_parsed = urllib.parse.urlparse(ercc_fa)
    if ercc_parsed.scheme not in ('http', 'https'):
        raise ValueError(f"Invalid ERCC FASTA URL scheme: {ercc_parsed.scheme}")
    tmp_fa = tempfile.NamedTemporaryFile(delete=False, suffix=".gz").name
    print(f"Downloading ERCC FASTA from {ercc_fa}")
    urllib.request.urlretrieve(ercc_fa, tmp_fa)
    with open(fasta_file, 'ab') as outfile, gzip.open(tmp_fa, 'rb') as infile:
        print(f"Appending ERCC FASTA data to {fasta_file}")
        outfile.write(infile.read())
    os.unlink(tmp_fa)
    
    ercc_gtf = ERCC_BUCKET + "ERCC92.gtf.gz"
    gtf_parsed = urllib.parse.urlparse(ercc_gtf)
    if gtf_parsed.scheme not in ('http', 'https'):
        raise ValueError(f"Invalid ERCC GTF URL scheme: {gtf_parsed.scheme}")
    tmp_gtf = tempfile.NamedTemporaryFile(delete=False, suffix=".gz").name
    print(f"Downloading ERCC GTF from {ercc_gtf}")
    urllib.request.urlretrieve(ercc_gtf, tmp_gtf)
    with open(gtf_file, 'ab') as outfile, gzip.open(tmp_gtf, 'rb') as infile:
        print(f"Appending ERCC GTF data to {gtf_file}")
        outfile.write(infile.read())
    os.unlink(tmp_gtf)

class MyParser(ArgumentParser):
    def error(self, message):
        self.print_help()
        galaxy_base = os.path.join(_get_data_dir(), "galaxy")
        print("\nCurrent genomes\n")
        print(open(loc.get_loc_file(galaxy_base, "samtools")).read())
        sys.exit(0)