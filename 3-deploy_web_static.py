
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
    date_time = datetime.now()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date_time.year,
        date_time.month,
        date_time.day,
        date_time.hour,
        date_time.minute,
        date_time.second
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
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
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
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)

