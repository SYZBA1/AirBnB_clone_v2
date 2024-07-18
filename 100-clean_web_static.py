#!/usr/bin/python3
# A Fabric script that deletes out-of-date archives.
import os
from fabric.api import *

env.hosts = ["100.26.243.119", "34.203.38.86"]


def do_clean(number=0):
    """Deletes out-of-date archives."""
    n = 1 if int(number) == 0 else int(number)

    archive = sorted(os.listdir("versions"))
    [archive.pop() for i in range(n)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archive]

    with cd("/data/web_static/releases"):
        archive = run("ls -tr").split()
        archive = [a for a in archive if "web_static_" in a]
        [archive.pop() for i in range(n)]
        [run("rm -rf ./{}".format(a)) for a in archive]
