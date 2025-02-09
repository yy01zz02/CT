    result = int(liney.strip().split()[1].strip('<>'))
    logger.debug("Got the job id: %s" % (str(result)))
    return result

def getjobexitcode(lsfJobID):
        job, task = lsfJobID
        
        #first try bjobs to find out job state
        args = ["bjobs", "-l", str(job)]
        logger.info("Checking job exit code for job via bjobs: " + str(job))
        process = subprocess.Popen(" ".join(args), shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        started = 0
        for line in process.stdout:
            if line.find("Done successfully") > -1:
                logger.info("bjobs detected job completed for job: " + str(job))
                return 0
            elif line.find("Completed <exit>") > -1:
                logger.info("bjobs detected job failed for job: " + str(job))
                return 1
            elif line.find("New job is waiting for scheduling") > -1: