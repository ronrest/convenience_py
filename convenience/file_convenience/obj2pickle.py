import pickle
def obj2pickle(obj, file):
    print("pickling object to {} ".format(file))
    with open(file, mode="wb") as fileObj:
        pickle.dump(obj, fileObj)
    print("---Done!")

