import cv2
import numpy as np


def convolution(img, filter):
    img_y, img_x = len(img), len(img[0])

    img_result = np.full((img_y, img_x), 0)

    for i in range(img_y):
        for j in range(img_x):
            temp = np.full((3, 3), 0)
            if i != 0 and j != 0 and i != img_y - 1 and j != img_x - 1:
                for filter_i in range(3):
                    for filter_j in range(3):
                        temp[filter_i][filter_j] = filter[filter_i][filter_j] * img[i + filter_i - 1][j + filter_j - 1] * 1/9
                img_result[i][j] = np.sum(temp)

    return img_result

if __name__ == '__main__':
    sobel_filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    prewitt_filter = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

    img = cv2.imread("filter.jpg", cv2.IMREAD_GRAYSCALE)
    sobel_x = convolution(img, sobel_filter)
    sobel_y = convolution(img, np.flip(sobel_filter.T, axis=0))

    prewitt_x = convolution(img, prewitt_filter)
    prewitt_y = convolution(img, np.flip(prewitt_filter.T, axis=0))

    prewitt = prewitt_x + prewitt_y
    sobel = sobel_x + sobel_y

    cv2.imwrite("sobel.png", sobel)
    cv2.imwrite("prewitt.png", prewitt)

