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
```py
################################################################################
#                                                    TOKENIZE AND VECTORIZE TEXT
################################################################################
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np

# SETTINGS
sequence_length = 100 # Fix the lenght of sequences
n_train = None        # Limit how much data to use for training
n_valid = 10000       # How many samples to set aside for validation
n_vocab = 10000       # set limit to maximum vocab size

# Create Vocabulary from corpus
tokenizer = Tokenizer(num_words=n_vocab)
tokenizer.fit_on_texts(data["X_train"])

# Convert corpus to sequences of word ids
data["X_train"] = tokenizer.texts_to_sequences(data["X_train"])
data["X_test"] = tokenizer.texts_to_sequences(data["X_test"])

# Restrict sequences to a max length
data["X_train"] = pad_sequences(data["X_train"], maxlen=sequence_length)
data["X_test"] = pad_sequences(data["X_test"], maxlen=sequence_length)


# Word and WOrd ID mappings
word2id = tokenizer.word_index
id2word = [""]*(len(word2id)+1) # keras tokenizer starts from 1, not 0
for word, id in word2id.items():
    id2word[id] = word


################################################################################
#                                    SHUFFLE DATA - And Create Validation Splits
################################################################################
# Shuffle Training data
np.random.seed(seed=345)
shuffled_indices = np.random.permutation(data["Y_train"].shape[0])
data["X_train"] = data["X_train"][shuffled_indices]
data["Y_train"] = data["Y_train"][shuffled_indices]

# Shuffle test data
np.random.seed(seed=345)
shuffled_indices = np.random.permutation(data["Y_test"].shape[0])
data["X_test"] = data["X_test"][shuffled_indices]
data["Y_test"] = data["Y_test"][shuffled_indices]

# Create Validation subset
if n_valid is not None:
    data["X_valid"] = data["X_train"][:n_valid]
    data["Y_valid"] = data["Y_train"][:n_valid]
    data["X_train"] = data["X_train"][n_valid:]
    data["Y_train"] = data["Y_train"][n_valid:]

# Limit train dataset
if n_train is not None:
    data["X_train"] = data["X_train"][:n_train]
    data["Y_train"] = data["Y_train"][:n_train]

# Print Summaries
print("Number of unique tokens in corpus =", len(word2id))
print("X_train: ", data["X_train"].shape)
print("Y_train: ", data["Y_train"].shape)
print("X_valid: ", data["X_valid"].shape)
print("Y_valid: ", data["Y_valid"].shape)
print("X_test: ", data["X_test"].shape)
print("Y_test: ", data["Y_test"].shape)
```
