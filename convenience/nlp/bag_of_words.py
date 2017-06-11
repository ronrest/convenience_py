import numpy as np


# ==============================================================================
#                                                            BAG OF WORDS VECTOR
# ==============================================================================
def bow_vector(doc, word_to_id, unknown_id=0, dtype=np.int32):
    """ Given a list of words `sentence` and the dictionary that maps words in
        the vocab to an array index, it returns an array which is
        a bag of words representation of that sentence.

        NOTE: Any words that are not in the vocabulary are assigned by
              default to the 0th index of the BOW. Change the `unknown_id`
              argument to set to a different index.

    Args:
        doc: (list of strings)
            List of words in the sentence, paragraph or document you wish to
            represent as a BoW vector.
        word_to_id: (dict)
            The dictionary that maps word strings to indices that will represent
            those words.
        unknown_id: (int, optional)(default=0)
            The index to use to represent words that do not appear in the
            vocabulary.
        dtype: (optional)(defualt=np.int32)
            The data type to use for the output array.

    Returns: (numpy array)
    """
    vec = np.zeros(len(word_to_id), dtype=dtype)  # Initialize BOW vector
    for word in doc:
        vec[word_to_id.get(word, unknown_id)] += 1
    return vec

