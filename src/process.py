import rawpy
import numpy as np
from PIL import Image

from src.demosaic import demosaic
from src.white_balance import gray_world
from src.gamma import gamma_correction


def process_raw(input_path, output_path):
    raw = rawpy.imread(input_path)
    rgb = demosaic(raw.raw_image_visible, pattern=raw.raw_pattern)
    rgb = gamma_correction(rgb, 1/2.2)
    rgb = gray_world(rgb)

    rgb /= 16383
    rgb_8bit = (rgb * 255).astype(np.uint8)

    img = Image.fromarray(rgb_8bit)
    img.save(output_path, quality=98)

