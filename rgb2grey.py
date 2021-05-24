import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
import os
   

path_img = './static/image.jpg'
path_img = os.path.relpath(path_img)

def imgTogrey():

    image = cv2.imread(path_img,cv2.IMREAD_UNCHANGED)
    #make mask of where the transparent bits are
    print(image.shape)
    trans_mask = image[:,:,3] == 0

    #replace areas of transparency with white and not transparent
    image[trans_mask] = [255, 255, 255, 255]

    #new image without alpha channel...
    new_img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path_img, gray)
