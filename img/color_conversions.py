def hex2rgb(s):
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
