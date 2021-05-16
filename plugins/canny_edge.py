import cv2 as cv


def filter_image(frame):
    return cv.Canny(frame, 125, 175)
