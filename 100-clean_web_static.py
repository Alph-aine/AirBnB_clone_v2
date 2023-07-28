#!/usr/bin/python3
""" clean up all outdated archives """

import os
from fabric.api import local, run, env, cd


env.hosts = ['18.204.10.145', '174.129.55.11']


def do_clean(number=0):
    """ deletes all out-dated archives locally and on the servers """
    number = int(number)
    if number <= 1:
        number = 1

    # get and delete archives on local machine
    archive_list = os.listdir("./versions")
    delete_list = archive_list[number:]
    for archive in delete_list:
        archive_path = os.path.join("./versions", archive)
        local(f'rm -rf {archive_path}')

    # get and deletes archives on servers
    with cd('/data/web_static/releases'):
        archive_list = run('ls -t | grep web_static').split()
        for archive in archive_list[number:]:
            run(f'rm -rf {archive}')
