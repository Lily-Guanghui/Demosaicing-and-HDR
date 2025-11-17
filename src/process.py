# For this task, we first used a basic method we had implemented earlier,
# but the results were not ideal. We then reviewed references and wrote a new
# function to handle contrast and saturation adjustments, and finally adopted a
# well-performing existing method. The basic version is commented out to keep the better result.




# import rawpy
# import numpy as np
# from PIL import Image

# from src.demosaic import demosaic
# from src.white_balance import gray_world
# from src.gamma import gamma_correction


# def process_raw(input_path, output_path):
#     raw = rawpy.imread(input_path)
#     rgb = demosaic(raw.raw_image_visible, pattern=raw.raw_pattern)
#     # sRGB standard display gamma ≈ 2.2
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
    """Process CR3 RAW files & output high-quality RGB images"""
    # Read RAW file & perform high-quality demosaicing
    with rawpy.imread(input_path) as raw:
        rgb = raw.postprocess(
            output_color=rawpy.ColorSpace.sRGB,
            use_camera_wb=True,
            demosaic_algorithm=rawpy.DemosaicAlgorithm.AHD,
            output_bps=8
        )
    
    # Convert to LAB color space for contrast enhancement
    lab = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB)
    
    # Apply CLAHE to the L channel for local contrast boost
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    lab[:,:,0] = clahe.apply(lab[:,:,0])
    
    # Convert back to RGB and slightly increase saturation
    enhanced = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
    hsv = cv2.cvtColor(enhanced, cv2.COLOR_RGB2HSV)
    hsv[:,:,1] = np.clip(hsv[:,:,1] * 1.1, 0, 255)
    final = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    
    # Save as a high-quality JPG
    Image.fromarray(final).save(output_path, 'JPEG', quality=99, optimize=True)