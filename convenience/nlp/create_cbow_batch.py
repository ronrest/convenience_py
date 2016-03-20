import numpy as np

def create_cbow_batch(size, window, ci, corpus):
    # --------------------------------------------------------------------------
    #                                                Get the context window size
    # --------------------------------------------------------------------------
    if isinstance(window, (int, long)):
        windowL = windowR = window
    elif isinstance(window, (list, tuple)) and len(window) == 2:
        windowL, windowR = window
    else:
        assert False, "`window` arg must be an integer or list of two integers"

    # --------------------------------------------------------------------------
    #                                                       Prepare batch arrays
    # --------------------------------------------------------------------------
    data_type = corpus.dtype
    center = np.ndarray(shape=(size), dtype=data_type)
    context = np.ndarray(shape=(size, windowL + windowR), dtype=data_type)

    # --------------------------------------------------------------------------
    #                        Create the Batch of center and context word indices
    # --------------------------------------------------------------------------
    corpus_size = len(corpus)
    for i, corpus_i in enumerate(range(ci, ci + size)):
        # Calculate corpus indices for center word, and context words.
        # Wrapping around the corpus if necessary.
        center_i = corpus_i % corpus_size
        context_i = range(corpus_i - windowL, corpus_i) + \
                     range(corpus_i + 1, corpus_i + windowR + 1)
        context_i = [index % corpus_size for index in context_i] # Wrap

        # Mapping corpus indices to the actual content contained at that point
        center[i] = corpus[center_i]
        context[i] = [corpus[index] for index in context_i]

    return center, context

