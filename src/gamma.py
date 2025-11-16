import numpy as np


def gamma_correction(data, gamma=0.3):
    a = np.percentile(data, 0.01)
    b = np.percentile(data, 99.99)
    data = (data - a) / (b - a)
    data[data < 0] = 0 
    data[data > 1] = 1
    
    # gamma correction
    data = data ** gamma
    data = data * (b - a) + a
    
    return data
