# src/ex6_hdr_merge.py

"""
Exercise 6: HDR merge

给定多张不同曝光的 LDR/linear 图像（同一场景），
估计 HDR radiance map。
"""

from typing import List, Tuple

import numpy as np

from .io_utils import save_image_uint8


def merge_hdr_linear(
    images_linear: List[np.ndarray],
    exposure_times: List[float],
) -> np.ndarray:
    """
    使用简单的加权平均，将多张不同曝光的图像合并为 HDR。

    Parameters
    ----------
    images_linear : list of np.ndarray
        每张为 H×W×3，已对齐且在同一线性空间
    exposure_times : list of float
        对应每张图像的曝光时间（秒）

    Returns
    -------
    hdr : np.ndarray
        H×W×3 浮点 HDR 图像（radiance map）
    """
    # TODO: 实现简单的 HDR 合并（例如 Robertsons / Debevec 的简化版，或者加权平均）
    raise NotImplementedError
