import numpy as np

def get_mockdata(n,m):

    return np.random.randint(500, 1000, size=(n,m))

data = get_mockdata(40, 3)
