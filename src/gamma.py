# import numpy as np


# def gamma_correction(data, gamma=0.3):
#   
#    #a = the darkest 0.01% pixel value
#    #b = the brightest 0.01% pixel value
#    #Map the intensity range to 0–1; clamp values below 0 to 0 and above 1 to 1


#     a = np.percentile(data, 0.01)
#     b = np.percentile(data, 99.99)
#     data = (data - a) / (b - a)
#     data[data < 0] = 0 
#     data[data > 1] = 1
    
#     # gamma correction
#     data = data ** gamma
#     data = data * (b - a) + a
    
#     return data

import numpy as np

def gamma_correction(data, gamma=0.3, method='power'):
#   a = the darkest 0.01% pixel value
#   b = the brightest 0.01% pixel value
#   Map the intensity range to 0–1; clamp values below 0 to 0 and above 1 to 1
    a = np.percentile(data, 0.01)
    b = np.percentile(data, 99.99)
    data = (data - a) / (b - a)
    data[data < 0] = 0 
    data[data > 1] = 1
    
    # gamma correction or other tone mapping
    if method == 'power':
        data = data ** gamma
    # Brighten shadows while compressing highlights
    elif method == 'log':
        data = np.log1p(9 * data) / np.log(10)
    else:
        raise ValueError("method must be 'power' or 'log'")
    
    data = data * (b - a) + a
    
    return data
