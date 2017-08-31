
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


# ==============================================================================
#                                                               CREATE_NGRAMS XY
# ==============================================================================
def create_ngrams_xy(doc, n=2):
    """ Given a list of words `doc`, it returns two lists, x and y.

        x = A list of lists, with each row being the first n-1 words of the
            ngram, which can be readily used as the input to a model.
        y = A list, with element being the nth word in the n gram, which can
            readily be used as the target label to be predicted.

    Examples:
        >>> doc = "once upon a time there lived a giant frog".split()
        >>> x,y = create_ngrams_xy(doc, n=3)
        >>> print(x)
        [['once', 'upon'],
         ['upon', 'a'],
         ['a', 'time'],
         ['time', 'there'],
         ['there', 'lived'],
         ['lived', 'a']]
        >>> print(y)
        ['a', 'time', 'there', 'lived', 'a', 'giant']
    """
    x = [[doc[j] for j in range(i, i + n - 1)] for i in range(0, len(doc) - n)]
    y = [doc[i + n - 1] for i in range(0, len(doc) - n)]
    return x, y

