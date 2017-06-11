import numpy as np


def bow_vector(doc, word_to_id, unknown_id=0, dtype=np.int32):
    vec = np.zeros(len(word_to_id), dtype=dtype)  # Initialize BOW vector
    for word in doc:
        vec[word_to_id.get(word, unknown_id)] += 1
    return vec

