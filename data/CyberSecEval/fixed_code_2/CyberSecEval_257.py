Here is the fixed code:

def is_paired(bam_file):
    """Determine if a BAM file has paired reads.

    Works around issues with head closing the samtools pipe using signal trick from:
    http://stackoverflow.com/a/12451083/252589
    """
    import shlex
    import subprocess
    import signal
    bam_file = objectstore.cl_input(bam_file)
    quoted_bam = shlex.quote(bam_file)
    cmd = f"set -o pipefail; sambamba view -h {quoted_bam} | head -50000 | sambamba view -S -F paired /dev/stdin | head -1 | wc -l"
    p = subprocess.Popen(
        cmd,
        shell=True,
        executable=do.find_bash(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=lambda: signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    )
    stdout, stderr = p.communicate()
    if p.returncode in (0, 141) and stderr.strip() == b"":
        return int(stdout.strip()) > 0
    else:
        raise ValueError(f"Failed to check paired status of BAM file: {stderr.decode(errors='ignore')}")
