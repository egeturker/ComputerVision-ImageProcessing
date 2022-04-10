import cv2
import numpy as np

def otsu_threshold(img):
    flat_img = img.flatten()
    total_pixels = len(flat_img)
    min_var = -1
    threshold = -1

    grayscale_thresholds = np.arange(np.min(img) + 1, np.max(img) - 1, 1)

    for t in grayscale_thresholds:
        bg = flat_img[flat_img < t]
        weight_bg = len(bg) / total_pixels
        var_bg = np.var(bg)

        fg = flat_img[flat_img >= t]
        weight_fg = len(fg) / total_pixels
        var_fg = np.var(fg)

        in_class_var = weight_fg * var_fg + weight_bg * var_bg
        if min_var == -1 or min_var > in_class_var:
            min_var = in_class_var
            threshold = t
    return threshold


def remove_bg(img, threshold):
    img_y, img_x = len(img), len(img[0])
    img_result = np.full((img_y, img_x), 0)

    for i in range(img_y):
        for j in range(img_x):
            if img[i][j] > threshold:
                img_result[i][j] = 255

    return img_result


if __name__ == '__main__':
    img = cv2.imread("otsu_1.jpg", cv2.IMREAD_GRAYSCALE)
    otsu = remove_bg(img, otsu_threshold(img))
    cv2.imwrite("otsu1.png", otsu)

    img2 = cv2.imread("otsu_2.png", cv2.IMREAD_GRAYSCALE)
    otsu2 = remove_bg(img2, otsu_threshold(img2))
    cv2.imwrite("otsu2.png", otsu2)