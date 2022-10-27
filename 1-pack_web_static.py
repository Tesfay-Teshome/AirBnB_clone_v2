#!/usr/bin/python3
""" Compress before sending """
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents
    of the web_static folder
    """
    try:
        today = datetime.now().strftime('%Y%m%d%H%M%S')
        path = "versions/web_static_{:s}.tgz".format(today)

        msg1 = "Packing web_static to {:s}".format(path)
        print(msg1)

        with hide('running'):
            local('mkdir -p ./versions')

        local('tar -cvzf {:s} web_static'.format(path))

        with hide('running'):
            size = local('wc -c < {:s}'.format(path), capture=True)

        msg2 = 'web_static packed: {:s} -> {:s}Bytes'.format(path, size)
        print(msg2)

        return path

    except:
        return None
