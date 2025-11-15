# src/ex1_bayer_patterns.py

"""
Exercise 1: Investigate Bayer Patterns

目标：
- 加载给定的 RAW / NPY 数据（例如 IMG_9939.npy）
- 根据彩色笔和背景，推断 Bayer pattern (RGGB, BGGR, GRBG, GBRG ...)
- 可视化各通道的采样位置，帮助理解 Bayer 布局
"""

from typing import Tuple

import numpy as np

from .io_utils import load_npy, save_image_uint8, show_image


def guess_bayer_pattern(raw: np.ndarray) -> str:
    """
    根据给定的 raw 图像，猜测 Bayer pattern。

    Parameters
    ----------
    raw : np.ndarray
        2D sensor data

    Returns
    -------
    pattern : str
        例如 "RGGB", "BGGR" 等
    """
    # TODO: 你和队友一起设计逻辑：
    # 1. 选取图像中包含红/绿/蓝笔的区域
    # 2. 查看不同位置像素的强度分布
    # 3. 推断每个位置对应的颜色
    raise NotImplementedError


def visualize_bayer_samples(raw: np.ndarray, pattern: str) -> np.ndarray:
    """
    生成一张可视化图，展示 Bayer 中 R/G/B 的位置。

    返回一个伪彩色图像，仅用于解释 pattern。
    """
    # TODO: 根据 pattern 构造一个 RGB 可视化图
    raise NotImplementedError


def run_ex1():
    """示例主函数，后面你可以在 main 或 notebook 里调用。"""
    raw = load_npy("IMG_9939.npy")  # 文件名视老师给的为准

    pattern = guess_bayer_pattern(raw)
    print(f"Guessed Bayer pattern: {pattern}")

    vis = visualize_bayer_samples(raw, pattern)
    save_image_uint8(vis, "ex1_bayer_pattern_visualization.png")
    show_image(vis, title=f"Bayer pattern: {pattern}")


if __name__ == "__main__":
    run_ex1()
