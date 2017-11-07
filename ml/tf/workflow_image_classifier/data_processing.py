import os
import pickle
import os

from image_processing import batch_preprocess

__author__ = "Ronny Restrepo"
__copyright__ = "Copyright 2017, Ronny Restrepo"
__credits__ = ["Ronny Restrepo"]
__license__ = "Apache License"
__version__ = "2.0"

# MAP LABELS AND IDS
id2label = ['class_0', 'class_1', 'class_2', 'class_3', 'class_4', 'class_5', 'class_6', 'class_7', 'class_8', 'class_9']
label2id = {val:id for id,val in enumerate(id2label)}

# ==============================================================================
#                                                                 MAYBE_MAKE_DIR
# ==============================================================================
def maybe_make_dir(path):
    """ Checks if a directory path exists on the system, if it does not, then
        it creates that directory (and any parent directories needed to
        create that directory)
    """
    if not os.path.exists(path):
        os.makedirs(path)

# ==============================================================================
#                                                                     GET_PARDIR
# ==============================================================================
def get_pardir(file):
    """ Given a file path, it returns the parent directory of that file. """
    return os.path.dirname(file)


# ==============================================================================
#                                                              MAYBE_MAKE_PARDIR
# ==============================================================================
def maybe_make_pardir(file):
    """ Takes a path to a file, and creates the necessary directory structure
        on the system to ensure that the parent directory exists (if it does
        not already exist)
    """
    pardir = os.path.dirname(file)
    if pardir.strip() != "": # ensure pardir is not an empty string
        if not os.path.exists(pardir):
            os.makedirs(pardir)


# ==============================================================================
#                                                                       FILE2STR
# ==============================================================================
def file2str(file):
    """ Takes a file path and returns the contents of that file as a string."""
    with open(file, "r") as textFile:
        return textFile.read()

# ==============================================================================
#                                                                       STR2FILE
# ==============================================================================
def str2file(s, file, mode="w"):
    """ Writes a string to a file"""
    # Ensure parent directory and necesary file structure exists
    pardir = os.path.dirname(file)
    if pardir.strip() != "": # ensure pardir is not an empty string
        if not os.path.exists(pardir):
            os.makedirs(pardir)

    with open(file, mode=mode) as textFile:
        textFile.write(s)


# ==============================================================================
#                                                                     OBJ2PICKLE
# ==============================================================================
def obj2pickle(obj, file, protocol=2):
    """ Saves an object as a binary pickle file to the desired file path. """
    # Ensure parent directory and necesary file structure exists
    pardir = os.path.dirname(file)
    if pardir.strip() != "": # ensure pardir is not an empty string
        if not os.path.exists(pardir):
            os.makedirs(pardir)

    with open(file, mode="wb") as fileObj:
        pickle.dump(obj, fileObj, protocol=protocol)


# ==============================================================================
#                                                                     PICKLE2OBJ
# ==============================================================================
def pickle2obj(file):
    """ Loads the contents of a pickle as a python object. """
    with open(file, mode = "rb") as fileObj:
        obj = pickle.load(fileObj)
    return obj


# ==============================================================================
#                                                               CREATE_DATA_DICT
# ==============================================================================
def create_data_dict(datadir):
    assert False, "NOT IMPLEMENTED: create_data_dict not yet created"


# ==============================================================================
#                                                                   PREPARE_DATA
# ==============================================================================
def prepare_data(data_file, valid_from_train=False, n_valid=1024, max_data=None, verbose=True):
    data = pickle2obj(data_file)

    # Create validation from train data
    if valid_from_train:
        data["X_valid"] = data["X_train"][:n_valid]
        data["Y_valid"] = data["Y_train"][:n_valid]
        data["X_train"] = data["X_train"][n_valid:]
        data["Y_train"] = data["Y_train"][n_valid:]

    if max_data:
        data["X_train"] = data["X_train"][:max_data]
        data["Y_train"] = data["Y_train"][:max_data]

    if verbose:
        # Print information about data
        print("DATA SHAPES")
        print("- X_valid: ", (data["X_valid"]).shape)
        print("- Y_valid: ", (data["Y_valid"]).shape)
        print("- X_train: ", (data["X_train"]).shape)
        print("- Y_train: ", (data["Y_train"]).shape)
        if "X_test" in data:
            print("- X_test: ", (data["X_test"]).shape)
        if "Y_test" in data:
            print("- Y_test: ", (data["Y_test"]).shape)

    return data


# ==============================================================================
#                                                           LOAD_BATCH_OF_IMAGES
# ==============================================================================
def load_batch_of_images(X_batch, img_shape=[299, 299]):
    batch = batch_preprocess(X_batch, shape=img_shape, mode="RGB")
    return batch


# ==============================================================================
#                                                        CALCULATE_CLASS_WEIGHTS
# ==============================================================================
def calculate_class_weights(Y, n_classes, method="paszke", c=1.02):
    """ Given the training data labels Calculates the class weights.

    Args:
        Y:      (numpy array) The training labels as class id integers.
                The shape does not matter, as long as each element represents
                a class id (ie, NOT one-hot-vectors).
        n_classes: (int) Number of possible classes.
        method: (str) The type of class weighting to use.

                - "paszke" = use the method from from Paszke et al 2016
                            `1/ln(c + class_probability)`
                - "eigen"  = use the method from Eigen & Fergus 2014.
                             `median_freq/class_freq`
                             where `class_freq` is based only on images that
                             actually contain that class.
                - "eigen2" = Similar to `eigen`, except that class_freq is
                             based on the frequency of the class in the
                             entire dataset, not just images where it occurs.
                -"logeigen2" = takes the log of "eigen2" method, so that
                            incredibly rare classes do not completely overpower
                            other values.
        c:      (float) Coefficient to use, when using paszke method.

    Returns:
        weights:    (numpy array) Array of shape [n_classes] assigning a
                    weight value to each class.

    References:
        Eigen & Fergus 2014: https://arxiv.org/abs/1411.4734
        Paszke et al 2016: https://arxiv.org/abs/1606.02147
    """
    # CLASS PROBABILITIES - based on empirical observation of data
    ids, counts = np.unique(Y, return_counts=True)
    n_pixels = Y.size
    p_class = np.zeros(n_classes)
    p_class[ids] = counts/n_pixels

    # CLASS WEIGHTS
    if method == "paszke":
        weights = 1/np.log(c+p_class)
    elif method == "eigen":
        assert False, "TODO: Implement eigen method"
        # TODO: Implement eigen method
        # where class_freq is the number of pixels of class c divided by
        # the total number of pixels in images where c is actually present,
        # and median freq is the median of these frequencies.
    elif method in {"eigen2", "logeigen2"}:
        epsilon = 1e-8 # to prevent division by 0
        median = np.median(p_class)
        weights = median/(p_class+epsilon)
        if method == "logeigen2":
            weights = np.log(weights+1)
    else:
        assert False, "Incorrect choice for method"

    return weights
