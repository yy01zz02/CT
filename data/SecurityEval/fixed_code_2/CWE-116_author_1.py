import os
import re
import stat
import pwd
import grp
from datetime import datetime
from flask import Response, request, Flask

app = Flask(__name__)

@app.route('/reply')
def listFiles():
    username = request.args.get("username")
    if not username:
        return Response("Username is required", status=400)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', username):
        return Response("Invalid username", status=400)
    dir_path = os.path.join('/home', username)
    if not os.path.isdir(dir_path):
        return Response("Directory not found", status=404)
    try:
        entries = []
        with os.scandir(dir_path) as dir_entries:
            for entry in dir_entries:
                stat_info = entry.stat()
                mode = stat.filemode(stat_info.st_mode)
                nlink = stat_info.st_nlink
                try:
                    owner = pwd.getpwuid(stat_info.st_uid).pw_name
                except KeyError:
                    owner = str(stat_info.st_uid)
                try:
                    group = grp.getgrgid(stat_info.st_gid).gr_name
                except KeyError:
                    group = str(stat_info.st_gid)
                size = stat_info.st_size
                mtime = datetime.fromtimestamp(stat_info.st_mtime).strftime('%b %d %H:%M')
                entries.append(f"{mode} {nlink} {owner} {group} {size} {mtime} {entry.name}")
        files_output = '\n'.join(entries)
    except Exception as e:
        return Response(f"Error listing directory: {e}", status=500)
    return Response(files_output)
