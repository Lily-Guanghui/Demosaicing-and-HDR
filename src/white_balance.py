import numpy as np


def gray_world(rgb):
    R = rgb[:, :, 0]
    G = rgb[:, :, 1]
    B = rgb[:, :, 2]

    gray = rgb.mean()

    R_wb = gray / R.mean() * R
    G_wb = gray / G.mean() * G
    B_wb = gray / B.mean() * B
    rgb_wb = np.stack([R_wb, G_wb, B_wb], axis=-1)

    rgb_wb = np.clip(rgb_wb, 0, 16383)

    return rgb_wb
