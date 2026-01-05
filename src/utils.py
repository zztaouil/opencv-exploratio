import cv2

import matplotlib.pyplot as plt
import numpy as np

def display_img(img, title=None):
    # converting color space BGR (default for cv2.imread) to RGB (what plt expects)
    # example color spaces: Grayscale, HSV (Hue, Saturation, Value),
    #   RGBA (Red, Green, Blue, Alpha)
    # https://opencv.org/blog/color-spaces-in-opencv/
    plt.title(title)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # plt.imshow(img[:,:,::-1])
    plt.axis('off')
    plt.show()

def display_mul_img(imgs, titles=None):
    if titles and len(imgs) != len(titles):
        return 1
    for i, img in enumerate(imgs):
        plt.subplot(1, len(imgs), 1 + i)
        if titles:
            plt.title(titles[i])
        plt.axis('off')
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
    return 0   

def draw_noise(img):
    pixels_nb = img.size // 5
    
    x = np.random.randint(0, img.shape[0], pixels_nb)
    y = np.random.randint(0, img.shape[1], pixels_nb)
    
    img[x, y] = [0, 0, 0]
    