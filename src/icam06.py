import numpy as np
from skimage.restoration import denoise_bilateral


def icam06_hdr(rgb, output_range=4, sigma_space=8, sigma_color=0.3):
    R = rgb[:, :, 0]
    G = rgb[:, :, 1]
    B = rgb[:, :, 2]
    # 加权平均得到亮度I，权重强调人眼敏感的颜色（或颜色对亮度的贡献）
    input_intensity = 1 / 61 * (20 * R + 40 * G + B)  
    # 得到色彩比
    R /= input_intensity
    G /= input_intensity
    B /= input_intensity

    # 用双边滤波平滑亮度
    log_I = np.log(input_intensity)
    log_base = denoise_bilateral(log_I, sigma_color=0.1, sigma_spatial=3)
    log_details = log_I - log_base   # 得到局部细节
    # 压缩亮度动态范围
    compression = np.log(output_range) / (log_base.max() - log_base.min())  # 计算压缩系数
    log_offset = - log_base.max() * compression  # 平移使亮度范围在 0~output_range
    output_intensity = np.exp(log_base * compression + log_offset + log_details)  #恢复指数得到最终亮度

    R *= output_intensity
    B *= output_intensity
    G *= output_intensity
    
    out = np.stack([R, G, B], axis=-1)

    return out
