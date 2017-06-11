import os
import numpy as np
import cv2

# kernel for sobel x
kernelx_sob = np.array([
    [-1,  0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])
# kernel for sobel y
kernely_sob = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])
# kernel for prewitt x
kernelx_prw = np.array([
    [-1,  0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])
# kernel for prewitt y
kernely_prw = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
])


def getRootDir():
    return os.path.dirname(os.path.abspath(__file__))


def displayImage(image,imageName):
    cv2.imshow(imageName, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def saveImage(image, name, path = "/images/saved_images/"):
    cv2.imwrite(getRootDir() + path + name, image)


def binary_threshold(image,thresval):
    return cv2.threshold(image, thresval, 255, cv2.THRESH_BINARY)[1]


def binary_inverse_threshold(image,thresval):
    return cv2.threshold(image, thresval, 255, cv2.THRESH_BINARY_INV)[1]


def otsu_threshold(image):
    ret, th = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return th


def gauss_otsu_threshold(image,ksize=5):
    image = cv2.GaussianBlur(image, (ksize, ksize), 0)
    return otsu_threshold(image)


def adapt_mean_threshold(image,blockSize=5,C=2):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, blockSize, C)


def adapt_gauss_threshold(image,blockSize=5,C=2):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, blockSize, C)