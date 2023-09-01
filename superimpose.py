import cv2
from PIL import Image

def superimpose_img(image_path, background_path, output_path) :
    
    input_image = Image.open(image_path)
    background_image = Image.open(background_path)
    
    input_image = input_image.resize((background_image.width, background_image.height))
    
    x = (background_image.width - input_image.width)//2
    y = (background_image.height - input_image.height)//2
    
    print(background_image.height, background_image.width)
    print(input_image.height, input_image.width)
    
    mask = input_image.convert("L")
    mask = mask.point(lambda p: p > 0 and 255)
    
    background_image.paste(input_image, (x,y), mask)
    background_image.save(output_path)