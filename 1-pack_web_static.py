#!/usr/bin/env python3
"""
a fabric script that generates a .tgz archive from the contents of the
web_static folder of the AirBnB Clone repo
"""

from fabric.operations import local
from datetime import datetime as dt


def do_pack():
    """ this function generates a .tgz archive """
    name = "versions/web_static_" + str(dt.now().year)
    name += str(dt.now().month) + str(dt.now().day) + str(dt.now().hour)
    name += str(dt.now().minute) + str(dt.now().second) + ".tgz"
    result = local("mkdir -p versions; tar -cvzf \"%s\" web_static" % name)
    if result.failed:
        return None
    else:
        return name
