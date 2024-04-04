#!/usr/bin/python3
"""script that deploys to webserver
"""
from fabric.api import env, put, run
from os.path import exists, join
from datetime import datetime
import os


env.hosts = ['54.237.13.137', '54.87.235.212']

env.key_filename = '/home/wasealex/.ssh/ssh_key'
env.user = 'ubuntu'


def do_pack():
    """ directory versions is created and web_static archive is saved
        All archives is stored in folder versions
        web_static_<year><month><day><hour><minute><second>.tgz is created
        if the archive has been correctly generated return the archive path.
        Otherwise, it should return None
    """
    local('mkdir -p versions')
    current_time = datetime.now()
    time_str = current_time.strftime('%Y%m%d%H%M%S')
    full_name = f'web_static_{time_str}.tgz'
    result = local(f'tar -cvzf versions/{full_name} web_static')
    file_path = join('versions', full_name)
    file_size = os.path.getsize(file_path)
    print(f"web_static packed: {file_path} -> {file_size} Bytes")
    if result.succeeded:
        return file_path
    return None


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    Uploads the archive to the /tmp/ directory of the web servers.
    Uncompresses the archive to the folder /data/web_static/releases/<archive
    filename without extension> on the web servers.
    Deletes the archive from the web servers.
    Deletes the symbolic link /data/web_static/current from the web servers.
    Creates a new symbolic link /data/web_static/current on the web servers,
    linked to the new version of the code.
    Returns True if all operations have been done correctly,
    otherwise returns False.
    """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archivename = os.path.basename(archive_path)
        archivefolder = '/data/web_static/releases/{}'.format(
            archivename.split('.')[0])
        run('mkdir -p {}'.format(archivefolder))
        run('tar -xzf /tmp/{} -C {}'.format(archivename, archivefolder))
        run('rm /tmp/{}'.format(archivename))

        run('mv {}/web_static/* {}'.format(archivefolder, archivefolder))
        run('rm -rf {}/web_static'.format(archivefolder))

        run('rm -rf /data/web_static/current')

        run('ln -s {} /data/web_static/current'.format(archivefolder))

        return True
    except Exception as e:
        return False
