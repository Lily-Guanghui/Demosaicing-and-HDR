# src/ex4_white_balance.py

"""
Exercise 4: White Balance

在 demosaicing + gamma 之后，对图像做 white balance（例如 gray world）。
"""

import numpy as np

from .io_utils import save_image_uint8, show_image


def gray_world_white_balance(rgb: np.ndarray) -> np.ndarray:
    """
    Gray-world 白平衡：让三通道平均值相等。

    Parameters
    ----------
    rgb : np.ndarray
        H×W×3 图像，[0,1] 或任意线性范围

    Returns
    -------
    balanced : np.ndarray
        白平衡后的图像（类型和范围和输入一致）
    """
    # TODO: 计算每个通道的平均值，然后用比例系数进行缩放
    raise NotImplementedError
