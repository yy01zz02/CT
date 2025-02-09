
    :param config_file_path:
    :return:
    """
    if config_file_path is None:
        config_dir_path = path.abspath(path.join(os.sep, path.dirname(__file__), path.pardir, 'config'))
        config_file_path = path.join(config_dir_path, '{}.config.yaml'.format(config_prefix))
        config_example_path = path.join(config_dir_path, '{}.example.yaml'.format(config_prefix))
        try:
            with open(config_file_path, 'rb') as config_stream:
                config_dict = yaml.load(config_stream, Loader=Loader)
        except IOError:
            logger.info('')
            try:
                os.makedirs(config_dir_path)
            except OSError as exc:
                if exc.errno == errno.EEXIST and path.isdir(config_dir_path):
                    pass
                else:
                    raise