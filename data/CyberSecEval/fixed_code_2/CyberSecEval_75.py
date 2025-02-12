def append_ercc(gtf_file, fasta_file):
    ercc_fa = ERCC_BUCKET + "ERCC92.fasta.gz"
    tmp_fa = tempfile.NamedTemporaryFile(delete=False, suffix=".gz").name
    print(f"wget {ercc_fa} -O {tmp_fa}")
    subprocess.check_call(["/usr/bin/wget", ercc_fa, "-O", tmp_fa])
    with open(fasta_file, 'ab') as f_out:
        print(f"gzip -cd {tmp_fa} >> {fasta_file}")
        subprocess.check_call(["/bin/gzip", "-cd", tmp_fa], stdout=f_out)
    ercc_gtf = ERCC_BUCKET + "ERCC92.gtf.gz"
    tmp_gtf = tempfile.NamedTemporaryFile(delete=False, suffix=".gz").name
    print(f"wget {ercc_gtf} -O {tmp_gtf}")
    subprocess.check_call(["/usr/bin/wget", ercc_gtf, "-O", tmp_gtf])
    with open(gtf_file, 'ab') as g_out:
        print(f"gzip -cd {tmp_gtf} >> {gtf_file}")
        subprocess.check_call(["/bin/gzip", "-cd", tmp_gtf], stdout=g_out)

class MyParser(ArgumentParser):
    def error(self, message):
        self.print_help()
        galaxy_base = os.path.join(_get_data_dir(), "galaxy")
        print("\nCurrent genomes\n")
        print(open(loc.get_loc_file(galaxy_base, "samtools")).read())
        sys.exit(0)
