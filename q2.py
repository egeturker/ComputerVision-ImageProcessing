import cv2
from matplotlib import pyplot as plt
import numpy as np

def histogram(img):
    img_y, img_x = len(img), len(img[0])
    h = np.full(256, 0)

    for i in range(img_y):
        for j in range(img_x):
            h[img[i][j]] += 1

    return h

if __name__ == '__main__':
    img = cv2.imread("grayscale_2.jpg", cv2.IMREAD_GRAYSCALE)
    hist = histogram(img)
    plt.plot(hist)
    plt.show()

    img2 = cv2.imread("grayscale_1.jpg", cv2.IMREAD_GRAYSCALE)
    hist2 = histogram(img2)
    plt.plot(hist2)
    plt.show()
