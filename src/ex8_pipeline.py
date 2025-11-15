# src/ex8_pipeline.py

"""
Exercise 8: process_raw(...) pipeline

把 Ex1~Ex7 串起来：从 RAW 开始一直到最终显示图像。
"""

from typing import List

import numpy as np

from .io_utils import load_npy, save_image_uint8
from .ex2_demosaicing import demosaic_bilinear
from .ex3_gamma_curve import apply_gamma
from .ex4_white_balance import gray_world_white_balance
from .ex6_hdr_merge import merge_hdr_linear
from .ex7_icam06 import tone_map_icam06


def process_single_raw_to_display(
    raw: np.ndarray,
    bayer_pattern: str,
    apply_wb: bool = True,
    apply_gamma_correction: bool = True,
) -> np.ndarray:
    """
    将单张 RAW 变成可显示的 LDR 图像。

    这将被 HDR pipeline 调用（先对每张曝光做 demosaic + WB 等）。 
    """
    # 1. demosaicing
    rgb_linear = demosaic_bilinear(raw, pattern=bayer_pattern)

    # 2. optional white balance
    if apply_wb:
        rgb_linear = gray_world_white_balance(rgb_linear)

    # 3. 归一化到 [0,1] 方便后续
    rgb_linear = rgb_linear / (rgb_linear.max() + 1e-8)

    # 4. optional gamma
    if apply_gamma_correction:
        rgb_display = apply_gamma(rgb_linear)
    else:
        rgb_display = rgb_linear

    return np.clip(rgb_display, 0.0, 1.0)


def process_exposure_stack_to_hdr(
    raws: List[np.ndarray],
    exposure_times: List[float],
    bayer_pattern: str,
) -> np.ndarray:
    """
    多张 RAW + 曝光时间 -> HDR radiance map。
    """
    # TODO: 调用 process_single_raw_to_display 或者一个 linear 版本，
    # 得到一组对齐的线性图像，再调用 merge_hdr_linear。
    raise NotImplementedError


def demo_pipeline():
    """
    一个简单 demo，展示如何使用上面的函数。
    你们以后可以在报告或小演示中用这个函数。
    """
    # TODO: 从 data/ 加载一组 RAW + 曝光时间，
    # 调用 process_exposure_stack_to_hdr，然后做 tone mapping。
    raise NotImplementedError


if __name__ == "__main__":
    demo_pipeline()
