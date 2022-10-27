#!/usr/bin/python3
""" Deploy Archive """
from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['44.200.170.122', '54.237.2.122']

env.user = "ubuntu"


def do_deploy(archive_path):
    """ deploy package """
    if archive_path is None or not os.path.isfile(archive_path):
        print("NOT PATH")
        return False

    aname = os.path.basename(archive_path)
    rname = aname.split(".")[0]

    put(local_path=archive_path, remote_path="/tmp/")
    run("mkdir -p /data/web_static/releases/{}".format(rname))
    run("tar -xzf /tmp/{} \
        -C /data/web_static/releases/{}".format(aname, rname))
    run("rm /tmp/{}".format(aname))
    run("rm -rf /data/web_static/current")
    run("ln -fs /data/web_static/releases/{}/ \
        /data/web_static/current".format(rname))
    run("mv /data/web_static/current/web_static/* /data/web_static/current/")
    run("rm -rf /data/web_static/curren/web_static")

    return True
