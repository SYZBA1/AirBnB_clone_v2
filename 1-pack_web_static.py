#!/usr/bin/python3
"""
    A script that generates a .tgz archivei from the contents of the
    web_static folder.
"""
import os
import tarfile
from datetime import datetime


def do_pack():
    """Creates a .tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    fd = "versions/web_static_{}.tgz".format(date)
    if not os.path.exists("versions/"):
        os.mkdir("versions/")
    with tarfile.open(fd, "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))
    if os.path.exists(fd):
        return fd
    else:
        return None
