import numpy as np
from scipy.signal import convolve2d

# creates three masks; pixels of the corresponding color are marked as 1, others as 0.
# Input should be the raw Bayer data and the Bayer pattern.
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

# interpolates each color channel using a convolution kernel.performs simple mean filtering: mask * RAW keeps only pixels of this color,&and pixels on other masks become 0.
# division normalizes the convolution result by the number of valid mask pixels， within the 3×3 neighborhood.
# Symmetric padding: boundary='symm'
def interpolate(X, mask):
    K = np.ones((3, 3))
    return convolve2d(mask * X, K, mode='same', boundary='symm') / convolve2d(mask, K, mode='same', boundary='symm')

# Final demosaicing function
def demosaic(X, pattern):
    M_R, M_G, M_B = mask_raw(X, pattern)
    R = interpolate(X, M_R)
    G = interpolate(X, M_G)
    B = interpolate(X, M_B)

# Stack the 3 color channels to form the final RGB image
    return np.stack([R, G, B], axis=-1)