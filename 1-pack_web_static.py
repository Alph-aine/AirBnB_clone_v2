#!/usr/bin/python3
""" creates an archive of a directory stored with the unique timestamp
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    ''' directory to store archives'''
    local("mkdir -p ./versions")

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = str("web_static_{}.tgz".format(time))

    # create archive
    result = local(f"tar -cvzf ./versions/{archive_name} ./web_static")

    if result.failed:
        return None
    else:
        return f'versions/{archive_name}'
