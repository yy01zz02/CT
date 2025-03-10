def copy_artifacts(source_path, destination_path):
    """

    :param source_path:
    :param destination_path:
    :return:
    """
    logging.info(
        'Moving model directory from {} to {}'.format(source_path,
                                                      destination_path))
    subprocess.call(
        ["/usr/bin/gsutil", "-m", "cp", "-r", "--", source_path, destination_path])


class AIPlatformModel(object):
    def __init__(self, project_id):
        self._project_id = project_id
        self._service = _create_service()