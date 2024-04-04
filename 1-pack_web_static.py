#!/usr/bin/python3
"""script that generates a .tgz archive
from the contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """ directory versions is created and web_static archive is saved
        All archives is stored in folder versions
        web_static_<year><month><day><hour><minute><second>.tgz is created
        if the archive has been correctly generated return the archive path.
        Otherwise, it should return None
    """
    local('sudo mkdir -p versions')
    current_time = datetime.now()
    time_str = current_time.strftime('%Y%m%d%H%M%S')
    full_name = f'web_static_{time_str}.tgz'
    result = local(f'sudo tar -cvzf versions/{full_name} web_static')
    file_size = os.path.getsize('versions/' + full_name)
    print(f"web_static packed: versions/{full_name} -> {file_size}Bytes")
    if result.failed:
        return None
    return f'versions/{full_name}'
