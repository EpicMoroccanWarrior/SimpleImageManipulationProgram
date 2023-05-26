# only works with .jpg files
import numpy as np
import matplotlib.pyplot as plt

def Invert(image_path): 
    image = plt.imread(image_path)
    return  255 - image

def flip_image_horizontally(image_path):
    image = plt.imread(image_path)
    flipped_image = np.flip(image, axis=1)   
    return flipped_image

def flip_image_vertically(image_path):
    image = plt.imread(image_path)
    flipped_image = np.flipud(image)
    return flipped_image

def grayscale_to_bw(image_path, threshold):
    image = plt.imread(image_path)
    bw_image = np.where(image >= threshold, 255, 0) 
    return bw_image

def add_black_frame(image_path, frame_width = 10):
    image = plt.imread(image_path)
    height, width, _ = image.shape
    framed_image = np.zeros((height + 2 * frame_width, width + 2 * frame_width, 3), dtype=np.uint8)
    framed_image[frame_width:-frame_width, frame_width:-frame_width, :] = image
    return framed_image


def display(img):
    plt.imshow(img)
    plt.axis("off")
    plt.show()
    
def show_image_in_mode(path, mode, threshold = 128, frame_width = 10):
    match mode:
        case "Invert":
            display(Invert(path))
        case "FlipHorizontal": 
            display(flip_image_horizontally(path))
        case "GrayscaleToBw": 
            display(grayscale_to_bw(path, threshold))
        case "FlipVertical": 
            display(flip_image_vertically(path))
        case "Frame":
            display(add_black_frame(path, frame_width))

def show_image(img):
    img = plt.imread(img)
    plt.imshow(img)
    plt.axis("off")
    plt.show()



