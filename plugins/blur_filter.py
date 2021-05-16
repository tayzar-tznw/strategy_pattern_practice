import cv2 as cv


def filter_image(frame):
    return cv.GaussianBlur(frame, (9, 9), cv.BORDER_DEFAULT)
