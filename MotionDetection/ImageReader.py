from PIL import ImageGrab
import numpy as np
import cv2
Image = np.array(ImageGrab.grab(bbox=(4, 326, 1280, 1045)))
while True:
    for y in range(len(Image)):
        for x in range(len(Image[y])):
            Image = np.array(ImageGrab.grab(bbox=(572, 615, 1848, 1333)))
            if Image[y][x][0] == 255 and Image[y][x][1]==0 and Image[y][x][2] == 255:
                print(x,y)
