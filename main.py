from remove_background import remove_bg
from superimpose import superimpose_img

import matplotlib.pyplot as plt
from PIL import Image

input_image_path = "image.jpg"
input_nobg_path = "no-background.png"
background_image_path = "background_image.jpg"
output_image_path = "output.jpg"

remove_bg(input_image_path, input_nobg_path)
superimpose_img(input_nobg_path, background_image_path, output_image_path)

plt.imshow(Image.open(output_image_path))
plt.show()
