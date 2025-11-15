# src/ex2_demosaicing.py

"""
Exercise 2: Demosaicing

给定 raw + Bayer pattern，输出线性 RGB 图像 (float, [0,1] 或原始范围)。

后续 Ex3/Ex4/Ex6 都会在此基础上继续处理，所以接口很重要。
"""

from typing import Tuple

import numpy as np

from .io_utils import load_npy, save_image_uint8, show_image


def demosaic_bilinear(raw: np.ndarray, pattern: str = "RGGB") -> np.ndarray:
    """
    用简单的 bilinear 插值做 demosaicing。

    Parameters
    ----------
    raw : np.ndarray
        2D raw sensor data
    pattern : str
        Bayer 模式，例如 "RGGB", "BGGR", "GRBG", "GBRG"

    Returns
    -------
    rgb : np.ndarray
        H×W×3 浮点图像，尚未 gamma 矫正、白平衡等。
    """
    # TODO: 你们在这里实现插值逻辑
    raise NotImplementedError


def run_ex2():
    """演示如何从 .npy 文件读取 raw 并做 demosaicing。"""
    raw = load_npy("IMG_XXXX.npy")  # 替换为实际文件名
    rgb = demosaic_bilinear(raw, pattern="RGGB")

    # 为了可视化，简单归一化
    rgb_norm = rgb / (rgb.max() + 1e-8)
    save_image_uint8(rgb_norm, "ex2_demosaic_result.png")
    show_image(rgb_norm, title="Ex2 Demosaic")


if __name__ == "__main__":
    run_ex2()
