# ==============================================================================
#                                                                       STR2FILE
# ==============================================================================
import os
def str2file(s, file, append=True, sep="\n"):
    """
    Takes a string object and a path to a file, and saves the contents of the
    string as text in the file. If the file does not already exist, a new file
    is created automatically.

    If the file already exists, then you can chose whether you want to append
    the new text to the file (this is the default behaviour), or replace the
    file altogether with the new content.

    If you chose to append, you can also chose how the new content gets
    separated from the existing content. By default, new content appears on a
    new line. But you could chose any other other string to separate the content
    or a blank string to make no separation at all.

    :param s: (string)
        The string containing the new content
    :param file: (string)
        The path to the file
    :param append: (bool)(default = True)
        Should it append new content to existing file? (or replace the file with
        new content)
    :param sep: (string)(default = "\n")
        The string used to separate the existing content with the new content.
    """
    # ==========================================================================
    mode = "a" if append else "w"    # Append or replace mode
    if append and (sep != ""):
        s = sep + s                  # Appended text separated by desired string

    # Ensure parent directory and necesary file structure exists
    pardir = os.path.dirname(file)
    if pardir.strip() != "": # ensure pardir is not an empty string
        if not os.path.exists(pardir):
            os.makedirs(pardir)

    with open(file, mode=mode) as textFile:
        textFile.write(s)
