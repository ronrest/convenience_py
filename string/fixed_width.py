# ==============================================================================
#                                                                    FIXED_WIDTH
# ==============================================================================
def fixed_width(s, width=80, remove_newlines=False, remove_leading_spaces=False):
    """ Given a string, it returns a new version of the string formatted
        so it has a maximim width of `width` characters. Is useful when
        viewing long strings in the console window.

    Args:
        s:               (string)
        width:           (int)
        remove_newlines: (bool) Remove the previous newlines?
    """
    s = s.rstrip() # remove trailing spaces
    pre = ""
    post = s
    output = []
    if remove_newlines:
        s = s.replace("\n", " ")

    while len(post) > 0:
        if remove_leading_spaces:
            s = s.lstrip()

        # With the  remaining text, take a chunk that is `width` chars long
        pre = s[:width]
        post = s[width:]
        newline = pre.find("\n")  # Get the position of any newline in this line

        # If no text is left over, then add the entire line
        if len(post) == 0:
            output.append(pre)
        # Handle newlines in the text.
        elif newline >= 0:
            output.append(s[:newline + 1])
            post = s[newline + 1:]
        elif pre.endswith(" "): # Safe to add whole line if ends in spacce
            output.append(pre[:-1])
        elif pre.endswith("\n"): # Safe to add if it ends in \n
            output.append(pre)
        elif post.startswith(" "): # Safe to add if post starts with " "
            post = post[1:]
            output.append(pre)
        else:                   # otherwise find a safe place to split the line
            # Find the previous space to end the line on.
            space_index = pre.rfind(" ")

            # If there is no previous space at all in the line, then just print
            # the entire line, splitting partway through some word.
            # But if there is previous space, then split at that point.
            if (space_index < 0):
                output.append(pre)
            else:
                pre = s[:space_index]
                post = s[space_index+1:]
                output.append(pre)
        s = post
    output = "\n".join(output)
    return output
