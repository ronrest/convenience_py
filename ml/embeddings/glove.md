# GloVe Word Embeddings

## Download
There are different embeddings that are trained on different text data.

- `glove.6B`
    - Wikipedia 2014 + Gigaword 5
    - 6B tokens, 400K vocab, uncased
    - 50d, 100d, 200d, & 300d vectors,
    - 822 MB download
    - URL = http://nlp.stanford.edu/data/glove.6B.zip

- `glove.42B.300d`
    - Common Crawl
    - 42B tokens, 1.9M vocab, uncased
    - 300d vectors,
    - 1.75 GB download
    - URL = http://nlp.stanford.edu/data/glove.42B.300d.zip

- `glove.840B.300d`
    - Common Crawl
    - 840B tokens, 2.2M vocab, cased
    - 300d vectors
    - 2.03 GB download
    - URL = http://nlp.stanford.edu/data/glove.840B.300d.zip

- `glove.twitter.27B`
    - Twitter
    - 2B tweets, 27B tokens, 1.2M vocab, uncased
    - 25d, 50d, 100d, & 200d vectors,
    - 1.42 GB download
    - URL = http://nlp.stanford.edu/data/glove.twitter.27B.zip
```

Use one of the embedding names from the above list, and download it by running wget on the command line.

```sh
# Chose embedding name (NOTE: no spaces on either side of the = sign)
EMBEDDING_NAME=glove.6B

# Download embeddings
BASE_URL=http://nlp.stanford.edu/data/
wget -c ${BASE_URL}${EMBEDDING_NAME}.zip

# Extract from zip file
unzip ${EMBEDDING_NAME}.zip -d ${EMBEDDING_NAME}
```

## Process in Python

The embeddings are stored in text file. Each line contains a single word followed by the embedding values, each separated by a space. A simplified example is as follows:

```
the -0.038194 -0.24487 0.72812 -0.39961 0.083172
and -0.071953 0.23127 0.023731 -0.50638 0.33923
....
```

### METHOD 1. Use the same ordering as GloVe embeddings file

```py
# TODO:
```


### METHOD 2. Use your own word ordering

**TODO:** Deal with "UNKNOWN" token

Given your own vocabulary that you have specified, and a mapping between word strings and their index, as in the following simplified example.

```py
id2word = ["king", "queen", "man", "woman", "lizard"]
word2id = {word:id for id, word in enumerate(id2word)}
```

Only extract embeddings for words that exist in your existing vocabulary.

```py
def create_glove_embeddings(embeddings_file, n_vocab, embedding_size, word2id, id2word, random_unknowns=True, verbose=True):
    """
    Creates a numpy array of GloVe embeddings from a text file.

    Args:
        embeddings_file: Path to the GloVe embeddings text file.
        n_vocab:         Size of vocabulary
        embedding_size:  Embedding vector size
        word2id:         dict mapping word strings to word ids
        id2word:         list mapping ids to word strings
        random_unknowns: (bool) whether to set the tokens not found in GloVe
                         to random weights.
        verbose:         (bool)

    Return:
        numpy array. Embeddings matrix of shape [n_vocab, embedding_size
    """
    # Initialize Embeddings
    embeddings = np.zeros([n_vocab, embedding_size], dtype=np.float32)

    # Extract embeddings from GloVe text file
    count = 0
    with open(embeddings_file, "r") as fileobj:
        for line in fileobj:
            # Separate the vector values from the word
            line = line.split()
            word = line[0]

            # If word is in our vocab, then update the corresponding weights
            id = word2id.get(word, None)
            if (id is not None) and (id < n_vocab):
                count += 1
                embeddings[id] = np.array(line[1:], dtype=np.float32)

    # Show a message if there are words that do not have embeddings
    if count < n_vocab:
        missing_ids = np.argwhere((embeddings==0).all(axis=1)).flatten()
        missing_words = [id2word[id] for id in missing_ids]
        if verbose:
            print("NOTE: {} words in vocab could NOT be located in embeddings file".format(n_vocab-count))
            print(missing_words)

        # Fix missing values, by assigning random values
        if random_unknowns:
            sd = 1/np.sqrt(embedding_size)
            for id in missing_ids[1:]: #skip the first zero vector
                embeddings[id] = np.random.normal(0, scale=sd, size=embedding_size)
    return embeddings



# Create the actual embeddings
embeddings_file = '/home/ronny/TEMP/gloVe/glove.6B/glove.6B.100d.txt'
embedding_size = 100

embeddings = create_glove_embeddings(embeddings_file=embeddings_file,
                            n_vocab=n_vocab,
                            embedding_size=embedding_size,
                            word2id=word2id,
                            id2word=id2word,
                            random_unknowns=True,
                            verbose=True)
```

## NOTES
Words containing apostrophes, such as

- `can't`
- `don't`
- `couldn't`

Appear in the vocabulary **without** the apostrophe. Be aware of this when performing tokenization of words.

Keras' built in tokenization object preserves the apostrophe. So be careful about using text tokenized with keras and using GloVe embeddings.


## Playing around with word vectors

Similarity between words

```py
def cosine_similarity(a,b):
    """ Cosine Similarity between two vectors"""
    return np.dot(a,b) / (np.linalg.norm(a, 2)*np.linalg.norm(b, 2))

def cosine_similarity_words(a, b):
    """ Given word strings, it finds the cosine similarity of the two
        word vectors that represent those words"""
    return cosine_similarity(embeddings[word2id[a]], embeddings[word2id[b]])

cosine_similarity_words("woman", "man") # 0.83234936
cosine_similarity_words("king", "queen") # 0.75076908
cosine_similarity_words("king", "lizard") # 0.23220986
```

Word vector arithmetic

```py
y = embeddings[word2id["king"]] - embeddings[word2id["man"]] + embeddings[word2id["woman"]]

queen = embeddings[word2id["queen"]]
lizard = embeddings[word2id["lizard"]]
cosine_similarity(y,queen) # 0.78344142
cosine_similarity(y,lizard) # 0.18114193
```
