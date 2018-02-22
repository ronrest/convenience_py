import os
import glob

def get_text_data_from_category_dirs(dataset_dir, id2label, ext="txt"):
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
