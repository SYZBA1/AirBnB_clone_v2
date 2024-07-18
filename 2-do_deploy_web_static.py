#!/usr/bin/python3
"""
    A script that distributes an archive to your web servers,
    using the function do_deploy
"""
import os
from fabric.api import env, local, put, run, runs_once
from datetime import datetime


env.hosts = ["100.26.243.119", "34.203.38.86"]
env.user = "ubuntu"

def do_deploy(archive_path):
    """
        Distributes an archive to a web server.
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    time = datetime.now()
    result = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second
    )
    try:
        print("Packing web_static to {}".format(result))
        local("tar -cvzf {} web_static".format(result))
        size = os.stat(result).st_size
        print("web_static packed: {} -> {} Bytes".format(result, size))
    except Exception:
        result = None
    return result


def do_deploy(archive_path):
    """
        Deploys the files to the host servers.
    """
    if not os.path.exists(archive_path):
        return False
    fd = os.path.basename(archive_path)
    dir_name = fd.replace(".tgz", "")
    dir_path = "/data/web_static/releases/{}/".format(dir_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(fd))
        run("mkdir -p {}".format(dir_path))
        run("tar -xzf /tmp/{} -C {}".format(fd, dir_path))
        run("rm -rf /tmp/{}".format(fd))
        run("mv {}web_static/* {}".format(dir_path, dir_path))
        run("rm -rf {}web_static".format(dir_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dir_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
