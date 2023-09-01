from remove_background import remove_bg
from superimpose import superimpose_img

import matplotlib.pyplot as plt

import cv2

input_image_path = "image.jpg"
input_nobg_path = "no-background.png"
background_image_path = "backround_image.jpg"
output_image_path = "output.jpg"

remove_bg(input_image_path, input_nobg_path)
superimpose_img(input_nobg_path, background_image_path, output_image_path)
# print(superimposed_image)

plt.imshow(cv2.imread(output_image_path))