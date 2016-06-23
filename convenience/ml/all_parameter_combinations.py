import itertools


# ==============================================================================
#                                                     ALL_PARAMETER_COMBINATIONS
# ==============================================================================
def all_parameter_combinations(d):
    """
    Takes a dictionary of lists, eg:
        d = {
            "type": ["a", "b"],
            "size": [10, 20]
           }

    and returns a list of dictionaries that explore all possible combinations of
    values, eg:
        [{'size': 10, 'type': 'a'},
         {'size': 20, 'type': 'a'},
         {'size': 10, 'type': 'b'},
         {'size': 20, 'type': 'b'}]

    :param d: (dictionary of lists)
        The dictionary, of lists of values to explore.
    :return: (list of dictionaries)
    """
    # ==========================================================================
    keys = d.keys()
    values = (d[varName] for varName in keys)
    combinations = [dict(zip(keys, combination)) for combination in
                    itertools.product(*values)]
    return combinations

