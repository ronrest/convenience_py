
def translate_strings(s, d):
    for key, val in d.items():
        s = s.replace(key, val)

    return s

