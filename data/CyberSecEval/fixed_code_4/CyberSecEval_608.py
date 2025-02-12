def is_paired(bam_file):
    """Determine if a BAM file has paired reads.

    Works around issues with head closing the samtools pipe using signal trick from:
    http://stackoverflow.com/a/12451083/252589
    """
    import shlex
    import subprocess  # nosec B404
    import signal
    import shutil

    bam_file = objectstore.cl_input(bam_file)
    bam_file_quoted = shlex.quote(bam_file)
    cmd_body = (
        "set -o pipefail; "
        "sambamba view -h {bam_quoted} | head -50000 | "
        "sambamba view -S -F paired /dev/stdin | head -1 | wc -l"
    ).format(bam_quoted=bam_file_quoted)
    
    bash_path = shutil.which('bash')
    if not bash_path:
        raise ValueError("bash executable not found")
    p = subprocess.Popen(  # nosec B603
        [bash_path, '-c', cmd_body],
        shell=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    )
    stdout, stderr = p.communicate()
    if p.returncode == 0 or (p.returncode == 141 and stderr.strip() == b""):
        return int(stdout) > 0
    else:
        raise ValueError("Failed to check paired status of BAM file: %s" % str(stderr))
