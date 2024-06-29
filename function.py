import numpy
def img_merge(back, img, sy, sx):#first - image formate RGBA(or numpy array [][][4]), second obsed y, third - obsed x
    sy = int(sy)
    sx = int(sx)
    im_out = numpy.copy(back)
    for a in range(img.shape[0]):
        for b in range(img.shape[1]):
            if(img.shape[2] == 4):
                if(img[a][b][3] == 255):
                    if(a + sy < back.shape[0] and a + sy >= 0) and (b + sx < back.shape[1] and b + sx >= 0):
                        im_out[a + sy][b + sx][0] = img[a][b][0]
                        im_out[a + sy][b + sx][1] = img[a][b][1]
                        im_out[a + sy][b + sx][2] = img[a][b][2]
            else:
                if(a + sy < back.shape[0] and a + sy >= 0) and (b + sx < back.shape[1] and b + sx >= 0):
                    im_out[a + sy][b + sx][0] = img[a][b][0]
                    im_out[a + sy][b + sx][1] = img[a][b][1]
                    im_out[a + sy][b + sx][2] = img[a][b][2]
    return im_out
def constrain(a, min, max):
    a = int(a)
    min = int(min)
    max = int(max)
    if a <= min:
        a = min
    elif a >= max:
        a = max-1
    return a
def place_that_you_cant_go(back):
    l = 0
    for a in range(back.shape[0]):
        print(back[a][0][3])
        if back[a][0][3] == 0:
            l = a
    return l
