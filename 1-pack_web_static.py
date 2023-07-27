#!/usr/bin/python3
''' creates an archive of a directory stored with the unique timestamp '''

from fabric import task
from datetime import datetime
import os


@task
def do_pack():
    ''' directory to store archives'''
    local("mkdir -p ./versions")

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = str("web_static_{}.tgz".format(time))

    # create archive
    result = os.system(f"tar -cvzf ./versions/{archive_name} ./web_static")

    if result.failed:
        return None
    else:
        return f'versions/{archive_name}'
