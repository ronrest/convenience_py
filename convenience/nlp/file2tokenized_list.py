from nltk import word_tokenize as tokenize


def file2tokenized_list(files, lower=True, encoding="utf-8"):
    print("Generating a tokenised list from files")
    if isinstance(files, dict):
        return dict_file2tokenized_list(files, lower, encoding)
    if isinstance(files, str):
        files = [files]
    num_items = len(files)

    tokenized_list = ["MISSING"] * num_items    # Will store the tokenised text
    for i in range(num_items):
        with open(files[i], "r") as textFile:
            text = textFile.read()
        text = text.decode(encoding)
        if lower:
            text = text.lower()
        tokenized_list[i] = tokenize(text)
    print("---Done!")
    return tokenized_list

file2tokenised_list = file2tokenized_list           # Non-US English version

