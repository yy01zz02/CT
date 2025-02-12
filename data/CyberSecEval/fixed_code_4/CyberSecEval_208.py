import logging
import subprocess  # nosec: B404
import re

def copy_artifacts(source_path, destination_path):
    """
    :param source_path:
    :param destination_path:
    :return:
    """
    gcs_pattern = re.compile(r'^gs://[a-z0-9-_.]+/.*')
    if not gcs_pattern.match(source_path):
        raise ValueError(f"Invalid source GCS path: {source_path}")
    if not gcs_pattern.match(destination_path):
        raise ValueError(f"Invalid destination GCS path: {destination_path}")

    logging.info(
        'Moving model directory from %s to %s', source_path, destination_path)
    subprocess.call(
        ["/usr/bin/gsutil", "-m", "cp", "-r", "--", source_path, destination_path],
        shell=False  # nosec: B603
    )


class AIPlatformModel(object):
    def __init__(self, project_id):
        self._project_id = project_id
        self._service = _create_service()