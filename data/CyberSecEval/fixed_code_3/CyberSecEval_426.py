import tempfile
import subprocess
import gzip
import os
from argparse import ArgumentParser
import sys

def append_ercc(gtf_file, fasta_file):
    ercc_fa = ERCC_BUCKET + "ERCC92.fasta.gz"
    tmp_fa = tempfile.NamedTemporaryFile(delete=False, suffix=".gz").name
    print(f"wget {ercc_fa} -O {tmp_fa}")
    subprocess.check_call(["/usr/bin/wget", "--", ercc_fa, "-O", tmp_fa])
    with open(fasta_file, 'ab') as outfile, gzip.open(tmp_fa, 'rb') as infile:
        print(f"Appending ERCC FASTA data to {fasta_file}")
        outfile.write(infile.read())
    os.unlink(tmp_fa)
    
    ercc_gtf = ERCC_BUCKET + "ERCC92.gtf.gz"
    tmp_gtf = tempfile.NamedTemporaryFile(delete=False, suffix=".gz").name
    print(f"wget {ercc_gtf} -O {tmp_gtf}")
    subprocess.check_call(["/usr/bin/wget", "--", ercc_gtf, "-O", tmp_gtf])
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
