import cv2 as cv


def filter_image(frame):
    return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
