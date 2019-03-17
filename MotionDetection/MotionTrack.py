import cv2
from PIL import ImageGrab, Image
import numpy as np

def main():

    w=800
    h=600

    cap = cv2.VideoCapture(0)

    cap.set(3, w)
    cap.set(4,h)

    print(cap.get(3))
    print(cap.get(4))

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = false

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    while ret:
        d = cv2.absdiff(frame1, frame2)

        g = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)

        b = cv2.GaussianBlur(g, (5, 5), 0)

        ret, th = cv2.threshold( b, 20, 255, cv2.THRESH_BINARY)

        contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        final = cv2.drawContours(frame1, contours, -1, (255, 0,255), 3)

        frame3 = frame1

        cv2.imshow("final", final)
        if cv2.waitKey(1) == 27:
            break

        frame1 = frame2
        ret, frame2 = cap.read()

    cv2.destroyAllWindows()
    cap.release()

if 1 == 1:
    main()
