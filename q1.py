import cv2
import numpy as np

element_x = 3
element_y = 3

def read_img(img_name):
    img = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    thresh = 127
    img_binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]
    return img_binary

def dilation(src_img, struct_et):
    img_y, img_x = len(src_img), len(src_img[0])
    struct_et_y, struct_et_x = len(struct_et), len(struct_et[0])
    struct_et_center_x, struct_et_center_y = (struct_et_x // 2, struct_et_y // 2)

    img_result = np.full((img_y, img_x), 255)

    found = False

    for i in range(img_y):
        for j in range(img_x):
            for struct_i in range(struct_et_y):
                for struct_j in range(struct_et_x):
                    comparison_i = i + struct_i - struct_et_center_x
                    comparison_j = j + struct_j - struct_et_center_y
                    if 0 <= comparison_i < img_y and 0 <= comparison_j < img_x:
                        if struct_et[struct_i][struct_j] == 1 \
                                and src_img[i + struct_i - struct_et_center_x][j + struct_j - struct_et_center_y] == 0:
                            img_result[i][j] = 0
                            found = True
                            break
                if found:
                    found = False
                    break

    return img_result


def erosion(src_img, struct_et):
    img_y, img_x = len(src_img), len(src_img[0])
    struct_et_y, struct_et_x = len(struct_et), len(struct_et[0])
    struct_et_center_x, struct_et_center_y = (struct_et_x // 2, struct_et_y // 2)

    img_result = np.full((img_y, img_x), 0)

    found = False

    for i in range(img_y):
        for j in range(img_x):
            for struct_i in range(struct_et_y):
                for struct_j in range(struct_et_x):
                    comparison_i = i + struct_i - struct_et_center_x
                    comparison_j = j + struct_j - struct_et_center_y
                    if 0 <= comparison_i < img_y and 0 <= comparison_j < img_x:
                        if struct_et[struct_i][struct_j] == 1 \
                                and src_img[i + struct_i - struct_et_center_x][j + struct_j - struct_et_center_y] == 255:
                            img_result[i][j] = 255
                            found = True
                            break
                if found:
                    found = False
                    break

    return img_result


if __name__ == '__main__':
    img = read_img('binary_image.png')
    struct_et = [[1 for _ in range(element_x)] for _ in range(element_y)]
    dilated_image = dilation(img, struct_et)
    eroded_image = erosion(img, struct_et)
    final_image = erosion(dilated_image, struct_et)

    cv2.imwrite("dilated.png", dilated_image)
    cv2.imwrite("eroded.png", eroded_image)
    cv2.imwrite("final.png", final_image)
