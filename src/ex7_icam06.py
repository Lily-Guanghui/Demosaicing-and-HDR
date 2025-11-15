# src/ex7_icam06.py

"""
Exercise 7: iCAM06 tone mapping

这里实现从 HDR -> 最终显示图像的 tone mapping。
可以只实现提交中真正需要的核心步骤。
"""

import numpy as np

from .io_utils import save_image_uint8, show_image


def tone_map_icam06(hdr: np.ndarray) -> np.ndarray:
    """
    对 HDR 图像应用简化版 iCAM06 tone mapping。

    Parameters
    ----------
    hdr : np.ndarray
        HDR 图像，H×W×3

    Returns
    -------
    ldr : np.ndarray
        适合 8-bit 显示的 LDR 图像，[0,1]
    """
    # TODO: 实现一个简化版流程（或老师要求的具体步骤）
    raise NotImplementedError
