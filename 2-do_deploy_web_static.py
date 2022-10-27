#!/usr/bin/python3
""" Deploy Archive """
from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['44.200.170.122', '54.237.2.122']

def do_deploy(archive_path):
    """Deployes the archive to the webserver"""
    if not exists(archive_path):
        return False

    full_name = archive_path.split("/")[1]
    file_name = archive_path.split("/")[1].split(".")[0]

    if put(archive_path, "/tmp/{}".format(
           full_name)).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/".format(
           file_name)).succeeded is False:
        return False

    if run("mkdir -p /data/web_static/releases/{}/".format(
           file_name)).succeeded is False:
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
           full_name, file_name)).succeeded is False:
        return False

    if run("rm /tmp/{}".format(full_name)).failed is True:
        return False

    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(file_name, file_name)
           ).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(file_name)).failed is True:
        return False

    if run("rm -rf /data/web_static/current").failed is True:
        return False

    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(file_name)).succeeded is False:
        return False

    return True
