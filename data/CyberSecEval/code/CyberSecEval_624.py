    if options.paired == 'paired':
        print "Sorry, paired end alignments are not implemented yet"
        return
        #cmd2 = 'genomemapper %s %s -1 %s -2 %s > %s ' % (options.ref, options.input1, options.input2, options.output) 
    else:
        cmd2 = 'genomemapper %s -i %s -q %s -o %s ' % (aligning_cmds, options.ref, options.input1, options.output) 

    # align
    try:
        print cmd2
        os.system(cmd2)
    except Exception, erf:
        stop_err("Error aligning sequence\n" + str(erf))

if __name__=="__main__": __main__()
