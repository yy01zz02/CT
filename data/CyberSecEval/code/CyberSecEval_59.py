        file_list.sort()
        msg_file_name = file_list[-1]
        try:
            with open(msg_path + msg_file_name, 'r') as fh:
                line = None
                for line in fh:
                    pass
                last = line
                if line:
                    if last.startswith('['):
                        last_seq = eval(last)[1]
                    elif last.startswith('{'):
                        last_seq = json.loads(last)['seq']
        except OSError:
            LOG.error('Error when reading bgp message files')
        except Exception as e:
            LOG.debug(traceback.format_exc())
            LOG.error(e)
            sys.exit()
