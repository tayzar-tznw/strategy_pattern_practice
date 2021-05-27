import cv2
import numpy as np


def filter_image(frame):
    image = cv2.imread("plugins/background.jpeg")
    image = cv2.resize(image, (850, 480))
    #
    # u_green = np.array([104, 153, 70])
    # l_green = np.array([30, 30, 0])

    l_green = np.array([100, 100, 100])
    u_green = np.array([250, 240, 240])

    mask = cv2.inRange(frame, l_green, u_green)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    f = frame - res
    f = np.where(f == 0, image, f)
    cv2.imshow("mask", frame)
    return f
