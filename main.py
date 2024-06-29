#pip3 install numpy
#pip3 install opencv-python
import cv2
#import numpy
from function import*
background = cv2.imread("background.png", -1)#background image
art = cv2.imread("test.png", -1)#front image
min_to_go = place_that_you_cant_go(background)
sm = 180
x, y = 0, 0#background.shape[0] // sm - 2
while 1:
    im_out = img_merge(background, art, y * sm, x * sm)#use function for merge image in one
    cv2.imshow("lol", im_out)#show image
    key = cv2.waitKey(0)
    if key == 27:
        break
    elif key == ord("w"):
        y = y - 1
    elif key == ord("s"):
        y = y + 1
    elif key == ord("d"):
        x = x + 1
    elif key == ord("a"):
        x = x - 1
    x = constrain(x, 0, background.shape[1] / sm)
    y = constrain(y, min_to_go/sm, background.shape[0] / sm)
    print(x, y)