import os
import shutil

def copyfile(source, destination):
    """ Copies file (ensuring necessary filestructure for destination exists)"""
    # Create the necessary parent directory structure
    pardir = os.path.dirname(destination)
    if pardir.strip() != "":    # ensure pardir is not an empty string
        if not os.path.exists(pardir):
            os.makedirs(pardir)

    # Now copy the file over
    shutil.copy2(source, destination)
