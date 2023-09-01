from rembg import remove
import cv2

def remove_bg(input_path, output_path):

    input_image = cv2.imread(input_path)
    output_image = remove(input_image)
    cv2.imwrite(output_path, output_image)