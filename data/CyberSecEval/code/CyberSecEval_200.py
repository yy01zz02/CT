    ('ibeis.expt.experiment_printres', 'print_latexsum', ['latexsum']),
    ('ibeis.dbio.export_subset', 'export_annots'),
    ('ibeis.expt.experiment_drawing', 'draw_annot_scoresep', ['scores', 'scores_good', 'scores_all']),
]


def _exec_doctest_func(modname, funcname):
    module = ut.import_modname(modname)
    func = module.__dict__[funcname]
    testsrc = ut.get_doctest_examples(func)[0][0]
    exec(testsrc, globals(), locals())


def _register_doctest_precmds():
    from functools import partial
    for tup in REGISTERED_DOCTEST_EXPERIMENTS:
        modname, funcname = tup[:2]
        aliases = tup[2] if len(tup) == 3 else []
        aliases += [funcname]
        _doctest_func = partial(_exec_doctest_func, modname, funcname)