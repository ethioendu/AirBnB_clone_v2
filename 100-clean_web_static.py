#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
import os
from fabric.api import *

env.hosts = ["34.234.204.250", "54.197.49.59"]


def do_clean(number=0):
    """Deletes out-of-date archives of the static files.

    Args:
        number (int): The number of archives to keep.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
