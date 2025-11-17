import numpy as np
from skimage.restoration import denoise_bilateral


def icam06_hdr(rgb, output_range=4, sigma_space=8, sigma_color=0.3):
    R = rgb[:, :, 0]
    G = rgb[:, :, 1]
    B = rgb[:, :, 2]
    # Compute luminance I using a weighted average that matches human visual sensitivity   input_intensity = 1 / 61 * (20 * R + 40 * G + B)  
    # Compute the chromaticity ratios
    R /= input_intensity
    G /= input_intensity
    B /= input_intensity

    # Smooth the luminance with a bilateral filter
    log_I = np.log(input_intensity)
    log_base = denoise_bilateral(log_I, sigma_color=0.1, sigma_spatial=3)
    # Extract local details
    log_details = log_I - log_base  
    # Compute the compression factor
    compression = np.log(output_range) / (log_base.max() - log_base.min())  
    # Shift the luminance range to 0~output_range
    log_offset = - log_base.max() * compression  
    # Recover the final luminance by applying the exponential mapping
    output_intensity = np.exp(log_base * compression + log_offset + log_details) 
    R *= output_intensity
    B *= output_intensity
    G *= output_intensity
    
    out = np.stack([R, G, B], axis=-1)

    return out
