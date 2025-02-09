    #
    # Development code
    RUN_DEV = True  # RUN_DEV = '__IPYTHON__' in vars()
    if RUN_DEV:
        dev_locals = run_dev(main_locals['ibs'])
        dev_execstr = utool.execstr_dict(dev_locals, 'dev_locals')
        exec(dev_execstr)

    command = ut.get_argval('--eval', type_=str, default=None)
    if command is not None:
        result = eval(command, globals(), locals())
        print('result = %r' % (result,))
        #ibs.search_annot_notes('360')

    #
    #
    # Main Loop (IPython interaction, or some exec loop)
    #if '--nopresent' not in sys.argv or '--noshow' in sys.argv:
    ut.show_if_requested()
    if ut.get_argflag(('--show', '--wshow')):