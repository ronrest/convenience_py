import os
import glob

def get_text_data_from_category_dirs(dataset_dir, id2label, ext="txt"):
    """
    Given a directory where the files containing the data are nested inside
    subdirectories representing a different class, it returns the string
    content of each file as a list of strings, and a second list with the
    corresponding label ids.

    Args:
        dataset_dir: (str) path to where the dataset is located
        id2label:    (list of str)
                      List of class label directory names, with each index
                      representing the class id.
                      eg ["cats", "dogs"]
        ext:         (str)(default="txt") Extension of the files to look for.

    Returns:
        X: (list of str) The string contents of each file
        Y: (list of int) The label ids for each file

    Note:
        Directory structure should look something like this:

        - dataset_dir
            - class0
                XXXX_Y.txt
                XXXX_Y.txt
                ...

            - class1
                XXXX_Y.txt
                XXXX_Y.txt
                ...
    """
    X = []
    Y = []
    for label_id, label in enumerate(id2label):
        subdir = os.path.join(dataset_dir, label)
        file_pattern = os.path.join(subdir, "*.{}".format(ext))
        for filepath in glob.glob(file_pattern):
            with open(filepath, "r") as fileobj:
                X.append(fileobj.read())

            Y.append(label_id)
    return X, Y
