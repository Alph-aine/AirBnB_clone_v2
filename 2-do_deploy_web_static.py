#!/usr/bin/python3
"""
Deploys web_static files to remote servers using fabric;
Uncompresses uploaded archive and deletes it
Deletes existing symlink for the web static and creates another
"""

from fabric.api import run, put, env
import os
import sys


env.hosts = ['18.204.10.145', '174.129.55.11']


def do_deploy(archive_path):
    """ checks if archive exist, uploads it,unpacks and deletes it,
        then create a new sylink for it
    """
    if not os.path.exists(archive_path):
        return False
    try:
        file = archive_path.split("/")[-1]
        # directory name to unpack the archive
        archive_file = file.split(".")[0]
        archive_dir = f"/data/web_static/releases/{archive_file}/"
        symlink = "/data/web_static/current"

        # deployment operatins
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(archive_dir))
        run('tar -xzf /tmp/{} -C {}'.format(file, archive_dir))
        run(f'rm -rf /tmp/{file}')
        run(f'mv {archive_dir}/web_static/* {archive_dir}')
        run(f'rm -rf {archive_dir}/web_static/')
        run(f'rm -rf {symlink}')
        run(f'ln -s {archive_dir} {symlink}')
        print('New version deployed')
        return True
    except (FileNotFoundError) as e:
        print(e)
        return False
