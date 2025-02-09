
        if len(qaid_list) > 0 or True:
            # Run the dev experiments
            expt_locals = run_devcmds(ibs, qaid_list, daid_list)
            # Add experiment locals to local namespace
            execstr_locals = utool.execstr_dict(expt_locals, 'expt_locals')
            exec(execstr_locals)
        if ut.get_argflag('--devmode'):
            # Execute the dev-func and add to local namespace
            devfunc_locals = devfunc(ibs, qaid_list)
            exec(utool.execstr_dict(devfunc_locals, 'devfunc_locals'))

    return locals()


#-------------
# EXAMPLE TEXT
#-------------

EXAMPLE_TEXT = '''