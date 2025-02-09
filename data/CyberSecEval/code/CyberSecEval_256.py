                os.makedirs(config_dir_path)
            except OSError as exc:
                if exc.errno == errno.EEXIST and path.isdir(config_dir_path):
                    pass
                else:
                    raise
            with open(config_file_path, 'a'):
                os.utime(config_file_path, None)
            try:
                with open(config_example_path, 'rb') as config_example_stream:
                    config_dict_example = yaml.load(config_example_stream, Loader=Loader)
                # TODO : console based example file modification
                with open(config_file_path, 'wb') as config_stream:
                    yaml.dump(config_dict_example, config_stream, Dumper=Dumper, encoding='utf-8')
            except IOError:
                logger.critical("No example file. Exiting.")
                sys.exit(0)
            try:
                with open(config_file_path, 'rb') as config_stream:
                    config_dict = yaml.load(config_stream, Loader=Loader)