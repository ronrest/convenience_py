
# ==============================================================================
#                                                                        HEX2RGB
# ==============================================================================
def hex2rgb(s):
    """ Given a color coded in hex code, eg `"#FF00FF"`, it returns
        the RGB pixel intensity representation of those values,
        scaled between 0-255
    Examples:
        >>> hex2rgb("#FF44AA")  # with hash notation
        (255, 68, 170)
        >>> hex2rgb("FF44AA")   # RGB
        (255, 68, 170)
        >>> hex2rgb("F4A")      # RGB compressed
        (255, 68, 170)
        >>> hex2rgb("FF44AAFF") # RGBA
        (255, 68, 170, 255)
        >>> hex2rgb("F4AF")      # RGBA compressed
        (255, 68, 170, 255)
    """
    if s.startswith("#"):
        s = s[1:]

    if len(s) == 6:
        return int(s[:2], 16), int(s[2:4], 16), int(s[4:6], 16)
    elif len(s) == 3:
        return int(s[0]+s[0], 16), int(s[1]+s[1], 16), int(s[2]+s[2], 16)
    elif len(s) == 4:
        return int(s[0]+s[0], 16), int(s[1]+s[1], 16), int(s[2]+s[2], 16), int(s[3]+s[3], 16)
    elif len(s) == 8:
        return int(s[:2], 16), int(s[2:4], 16), int(s[4:6], 16), int(s[6:8], 16)
