
# ==============================================================================
#                                                                  CREATE_NGRAMS
# ==============================================================================
def create_ngrams(doc, n=2):
    """ Given a list of words `doc`, it returns a list of ngrams, where
        each row contains a list of two elements:
        - A list of the first n-1 words
        - The final word

    Examples:
        >>> doc = "once upon a time there lived a giant frog".split()
        >>> create_ngrams(doc, n=3)
        [[['once', 'upon'], 'a'],
        [['upon', 'a'], 'time'],
        [['a', 'time'], 'there'],
        [['time', 'there'], 'lived'],
        [['there', 'lived'], 'a'],
        [['lived', 'a'], 'giant']]
    """
    ngrams = [[[doc[j] for j in range(i, i + n - 1)], doc[i + n - 1]] for i in
              range(0, len(doc) - n)]
    return ngrams

