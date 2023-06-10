import os
import cv2

imgs_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'imgs')
img_files = sorted([file for file in os.listdir(imgs_path) if file.endswith('.jpg')])

cur_img_index = -1

def get_next_img():
    global cur_img_index
    cur_img_index += 1
    if cur_img_index >= len(img_files):
        cur_img_index = 0

    return cv2.imread(os.path.join(imgs_path, img_files[cur_img_index]))
