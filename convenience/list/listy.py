

def listy(l, search=""):
    if isinstance(search, str):
        return [item for item in l if search.lower() in str(item).lower()]
    elif isinstance(search, (int, float, long)):
        return [item for item in l if search == item]

