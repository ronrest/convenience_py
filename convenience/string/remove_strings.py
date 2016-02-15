

def remove_strings(s, rem):
    for substring in rem:
        s = s.replace(substring, "")

    return s

