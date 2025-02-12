import os
import CTK
import tempfile
import stat
import time

UPLOAD_DIR = tempfile.gettempdir()

def ok(filename, target_dir, target_file, params):
    txt =  "<h1>It worked!</h1>"
    file_path = os.path.join(target_dir, target_file)
    try:
        stat_info = os.stat(file_path)
        permissions = stat.filemode(stat_info.st_mode)
        uid = stat_info.st_uid
        gid = stat_info.st_gid
        size = stat_info.st_size
        mtime_str = time.strftime('%b %d %H:%M', time.localtime(stat_info.st_mtime))
        ls_line = f"{permissions} {stat_info.st_nlink} {uid} {gid} {size} {mtime_str} {target_file}"
    except OSError as e:
        ls_line = f"Error: {e}"
    txt += f"<pre>{ls_line}</pre>"
    txt += "<p>Params: %s</p>" % (str(params))
    txt += "<p>Filename: %s</p>" % (filename)
    return txt

class default:
    def __init__(self):
        self.page = CTK.Page()
        self.page += CTK.RawHTML("<h1>Direct Upload with params</h1>")