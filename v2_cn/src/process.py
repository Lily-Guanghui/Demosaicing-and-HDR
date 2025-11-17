# 对于这道题，我们先选用了之前实现过的基础方法的整合，但是并不高级，效果也一般，所以我们又查阅资料编写了一个函数，完成了对比度和饱和度的处理等，并选用了现成且效果很好的方法调用，这里注释掉基础版本以得到更好结果
import rawpy
import numpy as np
from PIL import Image

from src.demosaic import demosaic
from src.white_balance import gray_world
from src.gamma import gamma_correction


def process_raw(input_path, output_path):
    raw = rawpy.imread(input_path)
    rgb = demosaic(raw.raw_image_visible, pattern=raw.raw_pattern)
    # sRGB 标准显示 gamma ≈ 2.2
    rgb = gamma_correction(rgb, 1/2.2)
    rgb = gray_world(rgb)

    rgb /= 16383
    rgb_8bit = (rgb * 255).astype(np.uint8)

    img = Image.fromarray(rgb_8bit)
    img.save(output_path, quality=98)

# # 我们对这个任务的理解是完成上述基本任务中的去马赛克，白平衡等步骤，再进行一些其他的优化处理，为了使结果更优，这里我们选用了一个现成的高级去马赛克算法
# import rawpy
# import numpy as np
# from PIL import Image
# import cv2

# def process_raw(input_path, output_path):
#     # 直接调用AHD去马赛克
#     with rawpy.imread(input_path) as raw:
#         rgb = raw.postprocess(
#             output_color=rawpy.ColorSpace.sRGB,       
#             use_camera_wb=True, # 使用相机自带白平衡
#             demosaic_algorithm=rawpy.DemosaicAlgorithm.AHD,
#             output_bps=8                               
#         )
    
#     # rgb-LAB，只处理亮度
#     lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB)
    
#     # 创建CLAHE对象，局部对比度增强
#     clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) 
#     lab[:,:,0] = clahe.apply(lab[:,:,0]) 
    
#     # lab-rgb
#     enhanced = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
    
#     # rgb-hsv,增强饱和度
#     hsv = cv2.cvtColor(enhanced, cv2.COLOR_RGB2HSV) 
#     hsv[:,:,1] = np.clip(hsv[:,:,1] * 1.1, 0, 255) # *1.1代表饱和度增加 10%
#     final = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)   
    
#     Image.fromarray(final).save(
#         output_path,       
#         'JPEG',       
#         quality=99,
#         optimize=True  
#     )
