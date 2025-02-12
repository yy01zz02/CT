import os
import CTK
import tempfile
import stat
import pwd
import grp
import time

UPLOAD_DIR = tempfile.gettempdir()

def ok(filename, target_dir, target_file, params):
    txt =  "<h1>It worked!</h1>"
    file_path = os.path.join(target_dir, target_file)
    
    try:
        st = os.stat(file_path)
        permissions = stat.filemode(st.st_mode)
        nlink = st.st_nlink
        uid = st.st_uid
        gid = st.st_gid
        
        try:
            user = pwd.getpwuid(uid).pw_name
        except KeyError:
            user = str(uid)
        
        try:
            group = grp.getgrgid(gid).gr_name
        except KeyError:
            group = str(gid)
        
        size = st.st_size
        mtime = time.strftime('%b %d %H:%M', time.localtime(st.st_mtime))
        ls_output = f"{permissions} {nlink} {user} {group} {size} {mtime} {target_file}"
    except Exception as e:
        ls_output = f"Error getting file info: {str(e)}"
    
    txt += f"<pre>{ls_output}</pre>"
    txt += f"<p>Params: {params}</p>"
    txt += f"<p>Filename: {filename}</p>"
    return txt

class default:
    def __init__(self):
        self.page = CTK.Page()
        self.page += CTK.RawHTML("<h1>Direct Upload with params</h1>")