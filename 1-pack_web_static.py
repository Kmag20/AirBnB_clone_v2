#!/usr/bin/env python3

from datetime import datetime
from fabric.api import local, run, env, puts
from fabric.contrib.files import exists
import os

def do_pack():
    """ Creates a .tgz archive from the contents of the
    web_static folder"""

    now = datetime.now()
    archive_name = f"web_static_{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}.tgz"

    # Create the versions folder if it doesn't exist
    if not exists("versions"):
        run("mkdir versions")

    # Create the archive
    with local.cd("web_static"):
        archive_path = os.path.join("../versions", archive_name)
        result = local("tar -cvzf {} .".format(archive_path))

    if result.succeeded:
        puts(f"Archive created successfully: {archive_path}")
        return archive_path
    else:
        puts(f"Failed to create archive")
        return None