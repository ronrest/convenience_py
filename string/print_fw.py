
# ==============================================================================
#                                                              PRINT FIXED WIDTH
# ==============================================================================
def print_fw(s, width=80):
    """
    Prints some string out with a fixed maximum width. Is useful when viewing
    long strings in the console window.

    :param s: (string)
    :param width: (int)
    """
    # ==========================================================================

    pre = ""
    post = s

    while len(post) > 0:
        pre = s[:width]
        post = s[width:]
        newline = pre.find("\n")  # check for occurence of newlines

        if len(post) == 0:      # If nothing left over, then print entire line
            print pre
        elif newline >= 0:      # handle newlines in the text.
            print s[:newline + 1]
            post = s[newline + 1:]
        elif pre.endswith(" "): # Safe to print whole line if ends in spacce
            print pre[:-1]
        elif pre.endswith("\n"): # Safe to print id ends in \n
            print pre
        elif post.startswith(" "): # Safe to print if post starts with " "
            post = post[1:]
            print pre
        else:                   # otherwise find a safe place to split the line
            # Find the previous space to end the line on.
            space_index = pre.rfind(" ")

            # If there is no previous space at all in the line, then just print
            # the entire line, splitting partway through some word.
            # But if there is previous space, then split at that point.
            if (space_index < 0):
                print pre
            else:
                pre = s[:space_index]
                post = s[space_index+1:]
                print pre
        s = post

