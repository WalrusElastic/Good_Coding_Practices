# This file a sample of the bad coding practices in place within SCVU. This is adapted from a real preprocessing script.
# Refactor this code, removing hardcoded variables, moving simple functions into a utils file, and grouping the large functionality into a class.


import cv2
import numpy as np

def convert_16bit_to_8bit_minmax(img_16bit: np.ndarray) -> np.ndarray:
    """Convert 16-bit image to 8-bit using min-max normalization."""
    img_float = img_16bit.astype(np.float32)
    min_val = np.min(img_float)
    max_val = np.max(img_float)
    
    if max_val == min_val:
        return np.zeros_like(img_float, dtype=np.uint8)
    
    img_8bit = 255 * (img_float - min_val) / (max_val - min_val)
    return img_8bit.astype(np.uint8)

def apply_cubic_convolution(img: np.ndarray, scale_factor: float) -> np.ndarray:
    """
    Resize image using cubic convolution interpolation.

    """
    new_h = int(img.shape[0] * scale_factor)
    new_w = int(img.shape[1] * scale_factor)
    return cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_CUBIC)


def preprocess_image(img_path: str) -> np.ndarray:

    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    img = apply_cubic_convolution(img, 2)
    img = convert_16bit_to_8bit_minmax(img)
    return img

def preprocess_all_images_in_folder(folder_path: str, output_folder: str, input_size: int = 512, output_size: int = 1024):
    import os
    from tqdm import tqdm

    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.tif', '.jpg'))]
    
    for image_file in tqdm(image_files, desc="Preprocessing images"):
        img_path = os.path.join(folder_path, image_file)
        processed_img = preprocess_image(img_path)
        
        output_path = os.path.join(output_folder, f"processed_{image_file}")
        cv2.imwrite(output_path, processed_img)