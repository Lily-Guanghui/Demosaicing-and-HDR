# src/io_utils.py

"""
通用的输入输出函数：加载/保存 RAW、PNG、Numpy 等。

所有其他模块尽量通过这里来访问数据路径，这样路径和命名统一。
"""

from pathlib import Path
from typing import Iterable, List, Tuple

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


# 项目根目录（假设 io_utils.py 位于 src/）
ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"
RESULTS_DIR = ROOT_DIR / "results"


def ensure_results_dir() -> None:
    """确保 results/ 目录存在。"""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def load_npy(name: str) -> np.ndarray:
    """
    从 data/ 目录加载 .npy 文件。

    Parameters
    ----------
    name : str
        文件名，例如 "IMG_9939.npy"

    Returns
    -------
    arr : np.ndarray
    """
    path = DATA_DIR / name
    return np.load(path)


def save_image_uint8(arr: np.ndarray, name: str) -> Path:
    """
    将 [0,1] 或 [0,255] 的图像保存为 uint8 PNG 到 results/。

    Parameters
    ----------
    arr : np.ndarray
        H×W 或 H×W×3 图像
    name : str
        输出文件名，例如 "ex2_demosaic.png"

    Returns
    -------
    path : Path
        保存的文件路径
    """
    ensure_results_dir()

    arr = np.asarray(arr)
    if arr.dtype != np.uint8:
        # 自动把 [0,1] 或浮点值映射到 [0,255]
        arr = np.clip(arr, 0.0, 1.0) * 255.0
        arr = arr.astype(np.uint8)

    out_path = RESULTS_DIR / name
    Image.fromarray(arr).save(out_path)
    print(f"[io_utils] Saved image to {out_path}")
    return out_path


def show_image(arr: np.ndarray, title: str = "", cmap: str | None = None) -> None:
    """简单显示图像（调试用）。"""
    plt.figure()
    if arr.ndim == 2:
        plt.imshow(arr, cmap=cmap or "gray")
    else:
        plt.imshow(arr)
    plt.title(title)
    plt.axis("off")
    plt.show()
