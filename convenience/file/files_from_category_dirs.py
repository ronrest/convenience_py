from __future__ import print_function
from dir_items import dir_items
import os.path as path


# ==============================================================================
#                                                       FILES_FROM_CATEGORY_DIRS
# ==============================================================================
def files_from_category_dirs(d, rel=True, root=""):
    """
    Where the data is stored as follows.

    _ parent_dir/
      |_ categoryA/
         |_ file1.ext
         |_ file2.ext
         |_ file3.ext

      |_ categoryB/
         |_ file1.ext
         |_ file2.ext
         |_ file3.ext

      |_ categoryC/
         |_ file1.ext
         |_ file2.ext
         |_ file3.ext

    Returns a dictionary:
     - Each key = a category.
     - the value associated with that key is a list of file paths for each of the
       files in that category.

    You can chose to return full file paths, paths relative to the parent
    directory, paths relative to some specified directory, or just the
    filenames by themselves.

    This is useful for machine learning, where you have each file being a
    training example, separated into different directories representing different
    classes, such as ham/spam, or positive/negative.

    :param d: (string)
        The parent directory.

    :param rel: (Bool) (default = True)
        Return relative file paths?
        If False, then returns absolute file paths

    :param root: (str or None)
        ""          : paths relative to the parent directory.
        "/my/path/" : paths of items relative to the selected directory
        None        : Just the file names, no paths.

    :return: (dict)
        Dictionary of lists of strings.
    """
    # ==========================================================================
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
