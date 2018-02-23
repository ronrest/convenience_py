# IMDB Movie review dataset

```py
from keras.datasets import imdb
from keras import preprocessing

n_vocab = 10000
sequence_length = 100
n_valid = 8000

(X_train, Y_train), (X_test, Y_test) = imdb.load_data(num_words=n_vocab, path="/home/ronny/TEMP/imdb/keras/imdb.npz")
word2id = imdb.get_word_index(path="/home/ronny/TEMP/imdb/keras/word2id.json")

# Clip sequences and pad
X_train = preprocessing.sequence.pad_sequences(X_train, maxlen=sequence_length)
X_test = preprocessing.sequence.pad_sequences(X_test, maxlen=sequence_length)

# Create validation split
X_valid = X_train[:n_valid]
Y_valid = Y_train[:n_valid]
X_train = X_train[n_valid:]
Y_train = Y_train[n_valid:]

print("Number of train examples: ", len(X_train))
print("Number of valid examples: ", len(X_valid))
print("Number of test  examples: ", len(X_test))
```
