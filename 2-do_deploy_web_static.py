#!/usr/bin/python3
"""script that deploys to webserver
"""
from fabric.api import env, put, run, sudo
from os.path import exists
import os


env.hosts = ['54.237.13.137', '54.87.235.212']

env.key_filename = '/home/wasealex/.ssh/ssh_key'
env.user = 'ubuntu'


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
        archivefolder = '/data/web_static/releases/' + archivename.split('.')[0]
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
