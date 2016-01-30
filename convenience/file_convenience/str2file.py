def str2file(s, file, append=True, sep="\n"):
    mode = "a" if append else "w"    # Append or replace mode
    if append and (sep != ""):
        s = sep + s                  # Appended text separated by desired string

    with open(file, mode=mode) as textFile:
        textFile.write(s)

