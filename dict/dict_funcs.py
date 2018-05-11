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

def mapdict(x, mapper):
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

class MapDict(object):
    # TODO: enable nested indexing
    # TODO: maybe find a way to have combined source indices.
    #       eg message_id, group_id >>> "{group_id}_{mesage_id}"
    def __init__(self):
        self.mapper = []

    def add(self, source, target, transformer=None):
        self.mapper.append((source, target, transformer))

    def map(self, d):
        return mapdict(d, self.mapper)

# dict_mapper = MapDict()
# dict_mapper.add("id", "message_id")
# dict_mapper.add("date", "time", lambda x: datetime2str(x, format="%Y-%m-%d %H:%M:%S", tz="UTC"))  # TODO: Prcess date
# dict_mapper.add("message", "text")
# dict_mapper.add("from_id", "author_id")
# dict_mapper.add("to_id", "group_id", lambda x: id_from_peerobject(x))
# message_dict = dict_mapper.map(input_message_dict)



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
