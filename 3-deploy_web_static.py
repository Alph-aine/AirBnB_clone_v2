#!/usr/bin/python3
"""
Full deployment - combining the do_pack adn do_deploy
"""
from datetime import datetime
from fabric.api import local, run, put, env
import os


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
        print(f'versions/{archive_name}')
        return f'versions/{archive_name}'


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
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return False


def deploy():
    archive_path = do_pack()
    if archive_path is None:
        return False
    return  do_deploy(archive_path)
