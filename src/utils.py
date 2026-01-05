import cv2

import matplotlib.pyplot as plt
import numpy as np

from random import randint

def display_img(img):
    # converting color space BGR (default for cv2.imread) to RGB (what plt expects)
    # example color spaces: Grayscale, HSV (Hue, Saturation, Value),
    #   RGBA (Red, Green, Blue, Alpha)
    # https://opencv.org/blog/color-spaces-in-opencv/
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # plt.imshow(img[:,:,::-1])
    plt.axis('off')
    plt.show()
 
def draw_noise(img):
    pixels_nb = img.size // 5
    
    x = np.random.randint(0, img.shape[0], pixels_nb)
    y = np.random.randint(0, img.shape[1], pixels_nb)
    
    img[x, y] = [0, 0, 0]
    