
def create_ngrams(doc, n=2):
    ngrams = [[[doc[j] for j in range(i, i + n - 1)], doc[i + n - 1]] for i in
              range(0, len(doc) - n)]
    return ngrams

