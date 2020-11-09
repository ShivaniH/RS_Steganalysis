import numpy as np
import cv2

def discrimination_function(np_img_window):
    np_img_window = np_img_window.flatten()
    return np.sum(np.abs(np_img_window[:-1] - np_img_window[1:]))

def flipping_operation(np_img_window, np_mask):
    pass