#!/usr/bin/python3
''' creates an archive of a directory stored with the unique timestamp '''

from fabric import task
from datetime import datetime
from fabric.api import local


@task
def do_pack():
    ''' directory to store archives'''
    local('mkdir -p ./versions')

    time = str(datetime.now().strftime("%Y%m%d%H%M%S"))
    archive_name = str('web_stattic_{}.tgz'.format(time))

    # create archive
    result = local(f'tar -cvzf versions/{archive_name} ./web_static')

    if result:
        return f'versions/{archive_name}'
    else:
        return None
