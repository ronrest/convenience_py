# IMDB Movie review dataset

## Download and extract data
```sh
wget http://s3.amazonaws.com/text-datasets/aclImdb.zip

# Extract only the useful subdirectory from zip file
unzip aclImdb.zip 'aclImdb/*'

# Rename extracted subdirectory
mv aclImdb imdb_raw
```

## Directory structure

```
- imdb_raw
    - train
        - neg
            XXXX_Y.txt
            XXXX_Y.txt
            XXXX_Y.txt
            ...
        - pos
            XXXX_Y.txt
            XXXX_Y.txt
            XXXX_Y.txt
            ...

    - test
        - neg
            XXXX_Y.txt
            XXXX_Y.txt
            XXXX_Y.txt
            ...
        - pos
            XXXX_Y.txt
            XXXX_Y.txt
            XXXX_Y.txt
            ...
```


## Loading in Python
```py
import os
import glob

datadir = "/home/ronny/TEMP/imdb/raw/imdb_raw"
train_dir = os.path.join(datadir, 'train')
train_dir = os.path.join(datadir, 'test')
id2label = ["neg", "pos"]

def get_text_data_from_category_dirs(dataset_dir, id2label, ext="txt"):
    """
    Given a directory where the files containing the data are nested inside
    subdirectories representing a different class, it returns the string
    content of each file as a list of strings, and a second list with the
    corresponding label ids.

    Args:
        dataset_dir: (str) path to where the dataset is located
        id2label:    (list of str)
                      List of class label directory names, with each index
                      representing the class id.
                      eg ["cats", "dogs"]
        ext:         (str)(default="txt") Extension of the files to look for.

    Returns:
        X: (list of str) The string contents of each file
        Y: (list of int) The label ids for each file
    """
    X = []
    Y = []
    for label_id, label in enumerate(id2label):
        subdir = os.path.join(dataset_dir, label)
        file_pattern = os.path.join(subdir, "*.{}".format(ext))
        for filepath in glob.glob(file_pattern):
            with open(filepath, "r") as fileobj:
                X.append(fileobj.read())

            Y.append(label_id)
    return X, Y


data = {}
data["X_train", "Y_train"] = get_text_data_from_category_dirs(train_dir, id2label, ext="txt")
data["X_test", "Y_test"] = get_text_data_from_category_dirs(test_dir, id2label, ext="txt")
```

## Tokenizing Text

**TODO:**
