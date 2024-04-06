#!/usr/bin/python3
"""
a Fabric script that distributes an archive to your web servers,
using the function do_deploy:
"""

import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once

env.hosts = ["34.234.204.250", "54.197.49.59"]


@runs_once
def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    dt = datetime.now()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year,
        dt.month,
        dt.day,
        dt.hour,
        dt.minute,
        dt.second
    )
    try:
        print("Packing web_static to {}".format(file))
        local("tar -cvzf {} web_static".format(file))
        archize_size = os.stat(file).st_size
        print("web_static packed: {} -> {} Bytes".format(file, archize_size))
    except Exception:
        file = None
    return file


def do_deploy(archive_path):
    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute..
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success

def deploy():
    """Archives and deploys the static files to the host servers.
    """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False
