import cv2
image = input()
image_conv = cv2.imread(image, -1)
image = image[:int(len(image))-4]
f = open(str(image + ".py"), 'w+')
f.write(str('#' + str(image_conv.shape[0]) + ' ' + str(image_conv.shape[1]) + '\n' + 'import numpy as np\n' + image + " = np.array(["))
for a in range(image_conv.shape[0]):
    f.write('[')
    for b in range(image_conv.shape[1]):
        f.write(str('[' + str(image_conv[a][b][0]) + ',' + str(image_conv[a][b][1]) + ',' + str(image_conv[a][b][2]) + ',' + str(image_conv[a][b][3]) + ']'))
        if b!= image_conv.shape[1]-1:
            f.write(',')
    f.write(']')
    if a!= image_conv.shape[0]-1:
        f.write(',')
f.write('])')