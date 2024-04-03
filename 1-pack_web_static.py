#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive from the
contents of the web_static folder of your AirBnB Clone repo.
"""

import os.path
from datetime import datetime
from fabric.api import local, runs_once


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
