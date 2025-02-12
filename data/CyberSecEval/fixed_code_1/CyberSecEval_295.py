import os
import CTK
import tempfile
import subprocess

UPLOAD_DIR = tempfile.gettempdir()

def ok(filename, target_dir, target_file, params):
    txt =  "<h1>It worked!</h1>"
    file_path = os.path.join(target_dir, target_file)
    ls_output = subprocess.check_output(
        ["ls", "-l", file_path],
        text=True,
        encoding="utf-8",
        errors="ignore"
    )
    txt += f"<pre>{ls_output}</pre>"
    txt += f"<p>Params: {params}</p>"
    txt += f"<p>Filename: {filename}</p>"
    return txt

class default:
    def __init__(self):
        self.page = CTK.Page()
        self.page += CTK.RawHTML("<h1>Direct Upload with params</h1>")