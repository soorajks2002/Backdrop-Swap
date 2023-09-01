import cv2
from PIL import Image

def superimpose_img(image_path, background_path, output_path) :
    
    # input_image = cv2.imread(image_path)
    # print(input_image.shape)
    # background_image = cv2.imread(background_path)
    # print(background_image.shape)
    
    input_image = Image.open(image_path)
    background_image = Image.open(background_path)
    
    x = (background_image.width - input_image.width)//2
    y = (background_image.height - input_image.height)//2
    
    
    mask = input_image.convert("L")  # Convert to grayscale
    mask = mask.point(lambda p: p > 0 and 255)
    
    background_image.paste(input_image, (x,y), mask)
    background_image.save(output_path)
    
    # output_image = cv2.addWeighted(input_image,1.0,background_image,1.0,0)
    
    # cv2.imwrite(output_path,output_image)