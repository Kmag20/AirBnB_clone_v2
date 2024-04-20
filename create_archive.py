#!/usr/bin/env python3
# fabric sucks

from datetime import datetime
import os

def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.
    """
    # Get the current timestamp
    now = datetime.now()
    archive_name = f"web_static_{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}.tgz"

    # Create the versions folder if it doesn't exist
    versions_dir = os.path.join(os.getcwd(), "versions")
    if not os.path.exists(versions_dir):
        os.makedirs(versions_dir)

    # Create the archive
    archive_path = os.path.join(versions_dir, archive_name)
    try:
        with os.popen(f"tar -cvzf {archive_path} -C web_static .") as p:
            p.read()
        print(f"Archive created successfully: {archive_path}")
        return archive_path
    except Exception as e:
        print("Failed to create archive")
        print(e)
        return None

do_pack()
