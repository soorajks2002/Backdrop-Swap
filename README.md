
# Backdrop Swap 📸

Backdrop-Swap: Background Replacement Tool

### Description:
Backdrop-Swap is a versatile and user-friendly tool designed to enable seamless background replacement for images. This project offers an intuitive interface for users to replace the background of any image effortlessly. 

### Key Features:

**1. Image Upload :** Users can upload two images - the target image (the one whose background they want to replace) and the new background image.

**2. Background Removal :** The tool employs advanced image segmentation techniques to automatically extract the main subject or character from the target image and create a transparent background.

**3. Resizing and Alignment :** The segmented image is resized to match the dimensions of the new background image, ensuring a perfect fit.

**4. Superimposition :** The segmented image with the transparent background is then superimposed onto the new background image, seamlessly blending the two to create a cohesive final image.

### How It Works:

**1. Image Selection :** Users select the target image and the new background image by uploading them through the user-friendly interface.

**2. Automated Segmentation :** Backdrop-Swap employs advanced image processing techniques to automatically segment the main subject from the target image, creating a precise mask.

**3. Background Replacement :** The tool superimposes the segmented subject onto the new background, ensuring a smooth transition and natural alignment using PIL.

### Benefits:

**1. Effortless Background Replacement :** Backdrop-Swap simplifies the complex process of background replacement, making it accessible to users without extensive image editing expertise.

**2. Automated Segmentation :** The tool's automated subject extraction ensures precise and accurate results, saving users time and effort.

**3. Perfect Fit :** By resizing and aligning the subject with the new background, Backdrop-Swap guarantees a visually appealing and natural-looking final image.

**4. Versatile Applications :** Users can leverage the tool for various purposes, such as enhancing product photos, creating artistic compositions, or adding creative elements to images.

##
**Backdrop-Swap** empowers users to transform their images by seamlessly replacing backgrounds. With its automated segmentation and precise alignment, it's a valuable tool for both creative professionals and individuals looking to enhance their visual content effortlessly.


## Demo

https://github.com/soorajks2002/Backdrop-Swap/assets/59795959/1b4b513a-7936-40aa-a567-49589ebfb066




## Run Locally

#### 1. Clone the project

```bash
  git clone https://github.com/soorajks2002/Backdrop-Swap.git
```

#### 2. Go to the project directory

```bash
  cd Backdrop-Swap
```

#### 3. Install packages

```bash
  pip install streamlit rembg Pillow
```

#### 4. Start the application
```bash
  streamlit run app.py
```


## Screenshots

![App Screenshot](https://github.com/soorajks2002/Backdrop-Swap/blob/main/Screenshots/Screenshot%201.png?raw=true)

![App Screenshot](https://github.com/soorajks2002/Backdrop-Swap/blob/main/Screenshots/Screenshot%202.png?raw=true)

![App Screenshot](https://github.com/soorajks2002/Backdrop-Swap/blob/main/Screenshots/Screenshot%203.png?raw=true)
