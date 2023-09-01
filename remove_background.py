from rembg import remove
import cv2

def remove_bg(input_path) :

    input_image = cv2.imread(input_path)
    output_image = remove(input_image)
    
    return output_image

print(remove_bg("test.jpg"))