import numpy as np

def discrimination_function(np_img_window):
    np_img_window = np_img_window.flatten()
    return np.sum(np.abs(np_img_window[:-1] - np_img_window[1:]))

def support_f_1(np_img_window):
    np_img_window = np.copy(np_img_window)
    even_indices = np_img_window % 2 == 0
    np_img_window[even_indices] += 1
    np_img_window[np.logical_not(even_indices)] -= 1
    return np_img_window
f_1 = lambda x: support_f_1(x)
f_0 = lambda x: x
f_neg1 = lambda x: support_f_1(x+1)-1
def flipping_operation(np_img_window, np_mask):
    np_result = np.empty(np_img_window.shape)
    dict_flip = {-1:f_neg1, 0:f_0, 1:f_1}
    for i in [-1, 0, 1]:
        temp_indices_x, temp_indices_y = np.where((np_mask == i) == True)
        np_result[temp_indices_x, temp_indices_y] = dict_flip[i](np_img_window[temp_indices_x, temp_indices_y])
    return np_result

def calculate_count_groups(np_img, np_mask):
    count_reg, count_sing = 0, 0
    for ih in range(0, np_img.shape[0], np_mask.shape[0]):
        for iw in range(0, np_img.shape[1], np_mask.shape[1]):
            np_img_window = np_img[ih: ih+np_mask.shape[0], iw: iw+np_mask.shape[1]]
            flipped_output = flipping_operation(np_img_window, np_mask)
            # print("Image window")
            # print(np_img_window)
            # print("Flipped version")
            # print(flipped_output)
            
            discrimination_img_window = discrimination_function(np_img_window)
            discrimination_flipped_output = discrimination_function(flipped_output)

            if discrimination_flipped_output > discrimination_img_window: count_reg += 1
            elif discrimination_flipped_output < discrimination_img_window: count_sing += 1
    return count_reg, count_sing