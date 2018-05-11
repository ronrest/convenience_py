
def nested_get(d, id):
    """ Given an indexable object such as a dict or a list/tuple,  and an
        index/key or list/tuple of keys/indices
        It dives into each key to retreive the nested item.

    Example:
    >>> mydict = {"people":{"jane":{"age":33}, "bob":{"age":24}}}
    >>> nested_get(mydict, ["people", "bob", "age"])
    24
    """
    if not isinstance(id, (list, tuple)):
        id = (id,)
    temp = d
    for key in id:
        temp = temp[key]
    return temp

def nested_insert():
    """ nested insertion. """
    assert False, "Not implemented yet"

def mapdict(x, mappers):
    """ Given a dictionary, and iterable of 3-tuples containing:
            (input_id, output_id, tranformation_func)
        it returns another dictionary whose values
        have been mapped and processed.
    Example:
    >>> mapper = []
    >>> mapper.append(["index", "id", None])
    >>> mapper.append(["message", "text", lambda x: x.lower()])
    >>> mapper.append(["height", "height", lambda x: x/100.])
    >>> mydict = {"index": 234, "message": "HELLO", "height": 173}
    >>> mapdict(mydict, mapper)
    {'height': 1.73, 'id': 234, 'text': 'hello'}
    """
    output = {}
    for source, target, transformer in mapper:
        if transformer is None:
            output[target] = x[source]
        else:
            assert callable(transformer), "transformer must be None or a callable"
            output[target] = transformer(x[source])
    return output

# def nested_mapdict(x, mappers):
#     """ Given a dictionary, and iterable of 3-tuples containing:
#             (input_id, output_id, tranformation_func)
#         it returns another dictionary whose values
#         have been mapped and processed. It evan allows for nested
#         indexing of source dictionary.
#         TODO: Add nesting
#     Example:
#     >>> mapper = []
#     >>> mapper.append(["index", "id", None])
#     >>> mapper.append(["message", "text", lambda x: x.lower()])
#     >>> mapper.append(["height", "height", lambda x: x/100.])
#     >>> mydict = {"index": 234, "message": "HELLO", "height": 173}
#     >>> mapdict(mydict, mapper)
#     {'height': 1.73, 'id': 234, 'text': 'hello'}
#     """
#     output = {}
#     for source, target, transformer in mapper:
#         if transformer is None:
#             output[target] = x[source]
#         else:
#             assert callable(transformer), "transformer must be None or a callable"
#             output[target] = transformer(x[source])
#     return output
