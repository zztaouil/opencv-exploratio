import cv2

import matplotlib.pyplot as plt
import numpy as np

from math import ceil


def display_img(img, title=None, color_space_flag=True):
    # converting color space BGR (default for cv2.imread) to RGB (what plt expects)
    # example color spaces: Grayscale, HSV (Hue, Saturation, Value),
    #   RGBA (Red, Green, Blue, Alpha)
    # https://opencv.org/blog/color-spaces-in-opencv/
    plt.title(title)
    if color_space_flag:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    # plt.imshow(img[:,:,::-1])
    plt.axis("off")
    plt.show()


def display_mul_img(imgs, titles=None, color_space_flag=True, rows_nb=1):
    if titles and len(imgs) != len(titles):
        return 1

    for i, img in enumerate(imgs):
        plt.subplot(rows_nb, ceil(len(imgs) / rows_nb), i + 1)
        if titles:
            plt.title(titles[i])
        if color_space_flag:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.axis("off")

    plt.tight_layout(pad=1.0)
    plt.show()
    return 0


def draw_noise(img):
    pixels_nb = img.size // 5

    x = np.random.randint(0, img.shape[0], pixels_nb)
    y = np.random.randint(0, img.shape[1], pixels_nb)

    img[x, y] = [0, 0, 0]


def draw_circle(img, coords, color=(0, 255, 0)):
    # Draw a point at each coordinate in the list
    for coord in coords:
        cv2.circle(img, (int(coord[0]), int(coord[1])), radius=20, color=color, thickness=-1)
