import itertools


def all_parameter_combinations(d):
    keys = d.keys()
    values = (d[varName] for varName in keys)
    combinations = [dict(zip(keys, combination)) for combination in
                    itertools.product(*values)]
    return combinations

