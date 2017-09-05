import os
import fnmatch


# ==============================================================================
#                                    RECURSIVELY FIND FILES THAT MATCH A PATTERN
# ==============================================================================
def search_files(root, pattern="*.jpg"):
    """ Search for files that match a pattern recursively through
        subdirectories. Includes hidden files and things in hidden
        directories that use the "." notation.
    """
    matches = []
    for curdir, dirnames, filenames in os.walk(root):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(curdir, filename))
    return matches
