import cv2 as cv
import loadmodule


def open_camera():
    filter_strategy = globals()['b']
    capture = cv.VideoCapture(0)

    while True:
        isTrue, frame = capture.read()

        cv.imshow('Camera', filter_strategy.filter_image(frame))

        key = cv.waitKey(20)
        if key != -1:
            filter_name = chr(key)
            if filter_name == 'd':
                break
            elif filter_name in globals():
                filter_strategy = globals()[filter_name]
            else:
                continue

    capture.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    loadmodule.do("plugins", globals())
    open_camera()
