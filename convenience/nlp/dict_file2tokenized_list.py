from nltk import word_tokenize as tokenize


def dict_file2tokenized_list(files, lower=True, encoding="utf-8"):
    cats = files.keys()
    num_per_category  = {cat: len(files[cat]) for cat in cats}
    num_items = sum(num_per_category.values())

    tokenized_list = ["MISSING"] * num_items    # Will store the tokenised text
    labels = ["MISSING"] * num_items            # Will store the labels

    running_index = 0
    for cat_i, cat in enumerate(cats):
        #num_items_for_cat =
        for example_i in range(num_per_category[cat]):
            with open(files[cat][example_i], "r") as textFile:
                text = textFile.read()
            text = text.decode(encoding)
            if lower:
                text = text.lower()
            tokenized_list[running_index] = tokenize(text)
            labels[running_index] = cat_i
            running_index += 1
    print("---Done!")
    return (tokenized_list, labels, cats)


dict_file2tokenised_list = dict_file2tokenized_list # Non-US English version

