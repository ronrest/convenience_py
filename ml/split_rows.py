"""====================================================
                    DESCRIPTION

=======================================================
"""
__author__ = 'ronny'

import numpy as np

# ==============================================================================
#                                                             ROW_SPLITTER_ARRAY
# ==============================================================================
def row_splitter_array(x, y=None, p=(0.6,0.2,0.2), seed=None):
    """
    Returns an array that randomly assigns the rows of some 2D array into
    several sub arrays. This can be useful to split training data for machine
    learning into a train, test and validation set.

    You specify the proportion of rows that you want assigned to each sub set
    using `p`.

    If you provide an array with output class labels `y`, then this function
    splits up the rows so as to preserve the ratio of each output class.

    NOTE: This does not actually split the `x` array, it simply returns a 1D
    array that provides integer values representing which subset that row
    should be assigned to.

    To actually split `x`, use the output of this function and feed it to the
    split_rows() function.

    :param x: {2D array}

        The 2D array that you want to split up.

    :param y: {None or 1D array} {Default = None}

        The class labels for each row of x.

    :param p: {tuple}{Default = (0.6,0.2,0.2)}

        What proportion of rows should be assigned to each subset. The values
        should add up to 1.

    :param seed: {None or int} {default = None}

        Set the seed of the random number generator used to assign rows to
        random subsets. This is useful if you want reproducible results.

    :return: {1D array}

        An array that is the same length as the number of rows in `x`, with
        each element being an integer in the range [0, num_subsets),
        representing which subset each row should be assigned to.

    :examples:
    splitter = row_splitter_array(X, y=Y, p=(0.6,0.2,0.2), seed=453)
    X_train, X_test, X_validate = split_rows(X, splitter)
    Y_train, Y_test, Y_validate = split_rows(Y, splitter)
    """
    # ==========================================================================
    num_rows = x.shape[0]
    num_splits = len(p)
    splitter = np.zeros(num_rows)  # Initialise the splitter array

    # Set the seed for reproducibility
    if seed is not None:
        np.random.seed(seed)

    # Group into output classes if `y` is provided
    if y is not None:
        classes = np.array(np.unique(y))
    else:
        classes = np.array([0])
        y = np.zeros(num_rows)

    # For each class, assign its elements to a random subset
    for class_i in classes:
        class_i_indices = np.where(y == class_i)[0] #indices of class i elements
        split_indices = np.random.choice(num_splits, size=len(class_i_indices),
                                         replace=True, p=p)
        splitter[class_i_indices] = split_indices
    return splitter


# ==============================================================================
#                                                                     SPLIT_ROWS
# ==============================================================================
def split_rows(x, splitter):
    """
    Splits up the rows of some 2D (or 1D) array into several sub arrays. This
    can be useful to split training data for machine learning into a train, test
    and validation set.

    Simply provide the array you want to split up, and a 1D array that specifies
    which subset each row should be assigned to, and it returns a tuple of
    arrays (one array for each subset specified in `splitter`.

    This is most useful when used in conjunction with the `row_splitter_array()`
    function. See the examples section to see how they are used together.

    :param x: {1D or 2D Array}

        The array containing the rows you want to split up

    :param splitter: {1D Array}

        A 1D array that is the same length as the number of rows in x,
        representing which subset each row should be assigned to.

    :return: {tuple}

        Returns a tuple of arrays that are subsets of x.

    :examples:
    splitter = row_splitter_array(X, y=Y, p=(0.6,0.2,0.2), seed=453)
    X_train, X_test, X_validate = split_rows(X, splitter)
    Y_train, Y_test, Y_validate = split_rows(Y, splitter)

    """
    # ==========================================================================
    subsets = ()
    for i in np.unique(splitter):
        subsets = subsets + (x[splitter == i], )
    return subsets
