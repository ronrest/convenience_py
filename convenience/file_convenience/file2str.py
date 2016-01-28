def file2str(file):
    with open(file, "r") as textFile:
        text = textFile.read()
    return text

