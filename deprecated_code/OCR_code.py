from PIL import Image, ImageOps, ImageFilter
import pytesseract
import re
import os
import cv2
import numpy as np

def load_image(image_path):
    """Loads an image using OpenCV."""
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at {image_path}")
    return img

def crop_profile_section(image):
    height, width, _ = image.shape
    
    #Top image
    profile_top_crop = int(height * 0.07) 
    profile_bottom_crop = int(height * 0.1)
    profile_left_crop = int(width * 0.22)
    profile_right_crop = int(width * 0.78)

    profile_img = image[
        profile_top_crop:profile_bottom_crop, 
        profile_left_crop:profile_right_crop]
    return profile_img

def to_grayscale(image):
    """Converts a BGR image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def denoise_image(image):
    """Applies median blurring for noise reduction."""
    # Kernel size 5 is common, adjust if needed
    # Tried 5, 3
    return cv2.medianBlur(image, 3)

def binarize_image(image):
    """Applies Otsu's thresholding for binarization."""
    # Use THRESH_OTSU for automatic threshold calculation
    # _, binary_img = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    _, binary_img = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
    return binary_img

def upscale_image(image, scale_factor=3):
    """Upscales an image using linear interpolation."""
    return cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

def binarize_image_adaptive(image):
    # ADAPTIVE_THRESH_GAUSSIAN_C or ADAPTIVE_THRESH_MEAN_C
    # blockSize: Size of a pixel neighborhood that is used to calculate a threshold value
    # C: Constant subtracted from the mean or weighted mean
    binary_img = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv2.THRESH_BINARY, 11, 2) # Adjust 11 and 2
    return binary_img

def denoise_image_gaussian(image):
    return cv2.GaussianBlur(image, (3, 3), 0) # Small kernel, 0 sigma for automatic

def preprocess_pipeline(image_path):
    """
    Applies a series of preprocessing steps optimized for TikTok profile OCR.
    """
    img = load_image(image_path)
    
    # 1. Crop to focus on the profile area
    cropped_img = crop_profile_section(img)
    upscaled_cropped_img = upscale_image(cropped_img, scale_factor=2)
    gray_img = to_grayscale(upscaled_cropped_img)
    denoised_img = denoise_image_gaussian(gray_img)
    binary_img = binarize_image_adaptive(denoised_img)

    return binary_img
def preprocessing_image(image_path):

    img = load_image(image_path)

    # name_img, bio_img = crop_profile(img)
    name_img = preprocess_pipeline(name_img)
    bio_img = preprocess_pipeline(bio_img)
