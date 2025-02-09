
SEQ_DIR = "seq"
RNASEQ_DIR = "rnaseq"
SRNASEQ_DIR = "srnaseq"

ERCC_BUCKET = "bcbio-data.s3.amazonaws.com/"

def extract_if_gzipped(filename):
    stem, ext = os.path.splitext(filename)
    if ext == ".gz":
        subprocess.check_call("gzip -cd %s > %s" % (filename, stem), shell=True)
        return stem
    else:
        return filename

def gff3_to_gtf(gff3_file):

    dialect = {'field separator': '; ',
               'fmt': 'gtf',
               'keyval separator': ' ',