# ==============================================================================
#                                  FILE2STR
# ==============================================================================
def file2str(file):
    """ Takes a file path and returns the contents of that file as a string.

    Args:
        file: (string)
            The path to the file.

    Returns: (string)
    """
    with open(file, "r") as textFile:
        text = textFile.read()
    return text


# ==============================================================================
#                                 TAIL
# ==============================================================================
import subprocess
def tail(f, n=10, offset=0):
    """ get the last few lines of a text file.
    NOTE: This will only work on a linux machine, since it relies on the
          `tail -f` command.
    Args:
        f:  (str) path to file
        n:  (int) number of lines to get
        offset: (int) skip this many lines from the end
    Returns:
        lines: (str)
    """
    proc = subprocess.Popen(['tail', '-n', str(n), f], stdout=subprocess.PIPE)
    # lines = proc.stdout.readlines() # get list of lines instead
    lines = proc.stdout.read()
    lines = str(lines, 'utf-8')
    return lines
