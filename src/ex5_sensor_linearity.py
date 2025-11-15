# src/ex5_sensor_linearity.py

"""
Exercise 5: Sensor linearity

给定多张不同曝光时间的 RAW / 灰卡图像，计算平均亮度，
并画出 "平均亮度 vs 曝光时间" 的曲线，检查线性程度。
"""

from typing import Iterable, List, Tuple

import numpy as np
from matplotlib import pyplot as plt

from .io_utils import load_npy, save_image_uint8, show_image, RESULTS_DIR, ensure_results_dir


def compute_mean_intensity(raw_images: List[np.ndarray]) -> np.ndarray:
    """
    对每张 raw 图像计算全图平均亮度。

    Returns
    -------
    means : np.ndarray
        shape = (N,)，N 为图像数量
    """
    # TODO: 按需要可以先截取 ROI 再取均值
    raise NotImplementedError


def plot_linearity(exposure_times: List[float], mean_values: np.ndarray):
    """
    绘制传感器响应曲线，并保存到 results/。
    """
    # TODO: 用 matplotlib 画折线/散点，检查是否近似直线
    raise NotImplementedError
