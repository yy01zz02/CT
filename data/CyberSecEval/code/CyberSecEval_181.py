              vis, logger=None, output_path=None):
    if not logger:
        assert False, 'require a logger'

    # print config
    pprint.pprint(config)
    logger.info('testing config:{}\n'.format(pprint.pformat(config)))

    # load symbol and testing data
    sym = eval('get_' + network + '_test')(num_classes=config.dataset.NUM_CLASSES)
    imdb = eval(dataset)(image_set, root_path, dataset_path, result_path=output_path)
    segdb = imdb.gt_segdb()

    # get test data iter
    test_data = TestDataLoader(segdb, batch_size=len(ctx))

    # load model
    # arg_params, aux_params = load_param(prefix, epoch, convert=True, ctx=ctx, process=True)
    arg_params, aux_params = load_param(prefix, epoch, process=True)
