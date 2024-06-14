#pip3 install numpy
#pip3 install opencv-python
import cv2
back = cv2.imread("background.png", -1)#back image
art = cv2.imread("art.png", -1)#front image
im_out = back#image that will be showed
def img_obed(img, sa, sb):#first - image formate RGBA, second obsed y, third - obsed x
    for a in range(img.shape[0]):
        for b in range(img.shape[1]):
            if(img.shape[2] == 4):
                if(img[a][b][3] == 255):
                    im_out[a + sa][b + sb][0] = img[a][b][0]
                    im_out[a + sa][b + sb][1] = img[a][b][1]
                    im_out[a + sa][b + sb][2] = img[a][b][2]
            else:
                im_out[a + sa][b + sb][0] = img[a][b][0]
                im_out[a + sa][b + sb][1] = img[a][b][1]
                im_out[a + sa][b + sb][2] = img[a][b][2]
    pass
img_obed(art, 100, 500)#use function for merge image in one
while 1:
    cv2.imshow("lol", im_out)#show image
    if cv2.waitKey(1) & 0xFF == 27:
        break
