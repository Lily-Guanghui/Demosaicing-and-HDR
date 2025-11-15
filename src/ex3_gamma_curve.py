# src/ex3_gamma_curve.py

"""
Exercise 3: Gamma / Tone curve

对线性 RGB 图像应用 gamma 矫正或其他简单 tone curve。
"""

from typing import Callable

import numpy as np
from matplotlib import pyplot as plt

from .io_utils import save_image_uint8, show_image


def apply_gamma(rgb_linear: np.ndarray, gamma: float = 1 / 2.2) -> np.ndarray:
    """
    对线性 RGB 图像应用 gamma 矫正。

    Parameters
    ----------
    rgb_linear : np.ndarray
        线性空间 RGB，假定已归一化到 [0,1]
    gamma : float
        gamma 指数（输出 = 输入 ** gamma）

    Returns
    -------
    rgb_display : np.ndarray
        适合显示/保存的 RGB (仍在 [0,1])
    """
    # TODO: 实现 gamma curve（注意防止负数）
    raise NotImplementedError


def plot_gamma_curve(gamma: float = 1 / 2.2, num_points: int = 256):
    """
    画出 gamma 曲线，帮助写报告。
    """
    # TODO: 实现曲线绘制，把图保存到 results/
    raise NotImplementedError
