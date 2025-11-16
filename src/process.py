# import rawpy
# import numpy as np
# from PIL import Image

# from src.demosaic import demosaic
# from src.white_balance import gray_world
# from src.gamma import gamma_correction


# def process_raw(input_path, output_path):
#     raw = rawpy.imread(input_path)
#     rgb = demosaic(raw.raw_image_visible, pattern=raw.raw_pattern)
#     # sRGB 标准显示 gamma ≈ 2.2
#     rgb = gamma_correction(rgb, 1/2.2)
#     rgb = gray_world(rgb)

#     rgb /= 16383
#     rgb_8bit = (rgb * 255).astype(np.uint8)

#     img = Image.fromarray(rgb_8bit)
#     img.save(output_path, quality=98)


import rawpy
import numpy as np
from PIL import Image
import cv2

def process_raw(input_path, output_path):
    """处理CR3 RAW文件并输出高质量RGB图像"""
    # 读取RAW文件并进行高质量去马赛克
    with rawpy.imread(input_path) as raw:
        rgb = raw.postprocess(
            output_color=rawpy.ColorSpace.sRGB,
            use_camera_wb=True,
            demosaic_algorithm=rawpy.DemosaicAlgorithm.AHD,
            output_bps=8
        )
    
    # 转换为LAB色彩空间进行对比度增强
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB)
    
    # 对亮度通道应用CLAHE增强局部对比度
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    lab[:,:,0] = clahe.apply(lab[:,:,0])
    
    # 转换回RGB并轻微增加饱和度
    enhanced = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
    hsv = cv2.cvtColor(enhanced, cv2.COLOR_RGB2HSV)
    hsv[:,:,1] = np.clip(hsv[:,:,1] * 1.1, 0, 255)
    final = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    
    # 保存为高质量JPG
    Image.fromarray(final).save(output_path, 'JPEG', quality=99, optimize=True)