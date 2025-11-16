import numpy as np
from scipy.signal import convolve2d


def mask_raw(bayer, pattern):
   H, W = bayer.shape
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


def interpolate(X, mask):
    K = np.ones((3, 3))
    return convolve2d(mask * X, K, mode='same', boundary='symm') / convolve2d(mask, K, mode='same', boundary='symm')


def demosaic(raw):
    X = raw.raw_image_visible
    pattern = raw.raw_pattern
    M_R, M_G, M_B = mask_raw(X, pattern)
    R = interpolate(X, M_R)
    G = interpolate(X, M_G)
    B = interpolate(X, M_B)

    return np.stack([R, G, B], axis=-1)