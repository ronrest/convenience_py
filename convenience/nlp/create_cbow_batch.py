import numpy as np

# ==============================================================================
#                                                              CREATE_CBOW_BATCH
# ==============================================================================
def create_cbow_batch(size, window, ci, corpus):
    """
    Creates a batch of center words and window context words for training CBOW.

    :param size: {int}
        The batch size.
    :param window: {int, or list of 2 ints}
        If it is an integer, it interprets it as the size of the window on each
        side symetrically (eg, 2 as a context window with 2 on the left, and 2
        on the right.

        If it is an list of two ints, then it interprets it as specifying
        the left and right windows separately.

    :param ci: {int}
        Corpus index. Where abouts in the corpus are we starting this batch?
    :param corpus: {Numpy array}
        The corpus as an 1D array, either as word strings or word indices.
    :return: {tuple}
        Returns a tuple with the following two elements:
        center  = A 1D array of the center words for the batch.
        context = A 2D array, with each row being the context words for the
                  batch.
    """
    # ==========================================================================
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

