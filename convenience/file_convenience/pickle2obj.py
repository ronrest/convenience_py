import pickle

def pickle2obj(file):
    with open(file, mode = "rb") as fileObj:
        obj = pickle.load(fileObj)
    return obj
