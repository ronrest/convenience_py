import os
import fnmatch


def search_files(root, pattern="*.jpg"):
    matches = []
    for curdir, dirnames, filenames in os.walk(root):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(curdir, filename))
    return matches
