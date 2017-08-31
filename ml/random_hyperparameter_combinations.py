import numpy as np

def random_hyperparameter_combinations(d, n):
    """ Given a dictionary `d` such as the following:

            d = {
                "SAMPLE_LENGTH": [200, 400, 800],
                "BATCH_SIZE": [32, 64, 128, 256],
                "N_HIDDEN": [64, 128, 256, 512],
                "EMBED_SIZE": [64, 128, 256, 512],
                "N_LAYERS": [1, 2, 3],
                "DROPOUT": [0.7],
                "ALPHA": [0.01, 0.1, 0.001, 0.0001]
                }
        which contains parameter names, and a list of possible values for
        each parameter. It returns a list of n unique dictionaries with
        key value pairs specifying a specific value for each parameter, eg:

            d = {
                "SAMPLE_LENGTH": 400,
                "BATCH_SIZE": 256,
                "N_HIDDEN": 64,
                "EMBED_SIZE": 256,
                "N_LAYERS": 3,
                "DROPOUT": 0.7,
                "ALPHA": 0.001
                }


    WARNING:
        This is a very naive implementation, it does not check to see
        if there is actually n possible combinations. If the total number
        of possible combinations is less than n, then it will get stuck in an
        infinite loop.
    """
    keys = d.keys()
    combinations = set()
    
    for _ in range(n):
        # Continue to create random combinations until it creates a new combination
        while True:
            combination = tuple(np.random.choice(d[key]) for key in keys)
            if combination not in combinations:
                combinations.add(combination)
                break
    
    list_of_hypers = []
    for vals in combinations:
        hyper = {key: vals[i] for i, key in enumerate(keys)}
        list_of_hypers.append(hyper)
    
    return list_of_hypers

