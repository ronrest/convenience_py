from __future__ import print_function
from dir_items import dir_items
import os.path as path


def files_from_category_dirs(d, rel=True, root=""):
    print("Retrieving category dir file paths from: {}".format(d))
    categories = dir_items(d, opt="dirs", rel=True)

    # Will store a list of file paths for each category
    files = {key: [] for key in categories}

    if root == "":
        root = d
    elif root is None:  # used to get just the file names
        root = ""

    for subdir in files.keys():    # used to get paths relative to parent directory
        files[subdir] = dir_items(path.join(d, subdir), opt="files",
                               rel=rel, root=root)
    print("---Done!")
    return files
