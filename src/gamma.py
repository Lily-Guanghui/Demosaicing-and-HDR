# import numpy as np


# def gamma_correction(data, gamma=0.3):
#     # a = 最暗的0.01%像素值
#     # b = 最亮的0.01%像素值
#     # 将亮度范围映射到0-1之间，低于0的设为0，高于1的设为1
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
    # a = 最暗的0.01%像素值
    # b = 最亮的0.01%像素值
    # 将亮度范围映射到0-1之间，低于0的设为0，高于1的设为1
    a = np.percentile(data, 0.01)
    b = np.percentile(data, 99.99)
    data = (data - a) / (b - a)
    data[data < 0] = 0 
    data[data > 1] = 1
    
    # gamma correction 或其他映射
    if method == 'power':
        data = data ** gamma
    # 暗部拉亮，同时压缩亮部
    elif method == 'log':
        data = np.log1p(9 * data) / np.log(10)
    else:
        raise ValueError("method must be 'power' or 'log'")
    
    data = data * (b - a) + a
    
    return data
