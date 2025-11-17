import numpy as np
from scipy.signal import convolve2d

# 这一步相当于创建了三张布，在对应颜色的布上将颜色标为1，否则为0，这里要传入原始拜耳数据和拜耳模式
def mask_raw(bayer, pattern):
   R = np.zeros_like(bayer)
   G = np.zeros_like(bayer)
   B = np.zeros_like(bayer)

   for i in range(2):
      for j in range(2):
         ch = pattern[i, j]
         if ch == 0:
            R[i::2, j::2] = 1
         elif ch == 2:
            B[i::2, j::2] = 1
         else:
            G[i::2, j::2] = 1

   return R, G, B

# 这一步是对每个颜色通道进行插值，使用卷积核对缺失的像素进行估计，这里使用的是简单的均值滤波，相当于把mask的结果要乘原RAW的值，并且把非这块布的颜色变为0
# 这里的大除法是在平均卷积后的结果（也就是卷积的值除以3*3范围内有效参与卷积的mask数）
# 对称填充boundary = 'symm'，
def interpolate(X, mask):
    K = np.ones((3, 3))
    return convolve2d(mask * X, K, mode='same', boundary='symm') / convolve2d(mask, K, mode='same', boundary='symm')

# 最终的去马赛克函数
def demosaic(X, pattern):
    M_R, M_G, M_B = mask_raw(X, pattern)
    R = interpolate(X, M_R)
    G = interpolate(X, M_G)
    B = interpolate(X, M_B)

# 将三个通道堆叠在一起，形成最终的RGB图像
    return np.stack([R, G, B], axis=-1)