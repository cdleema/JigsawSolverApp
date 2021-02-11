import cv2
import numpy
import sys
import os


list_arg = sys.argv

cur_path = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(cur_path, list_arg[1])
##print(os.path.exists(img_path))
##print('image path: %s' % img_path)
is_colour = 1 #Black and White

try:
    if list_arg[2] is True:
        is_colour = 2; #Colour
except:
    is_colour = 1

try:
    img = cv2.imread(img_path, is_colour)
    # img stored as bgr

    img_len = len(img) # y-axis
    img_wid = len(img[0]) #x-axis
    img_dim = len(img[0][0]) #colour-axis (z)

    # removing the 
    for i in range(img_len):
        for j in range(img_wid):
            img[i,j,0] = 0
            img[i,j,2] = 0
    cv2.imshow('name',img)
    print('l: %i w:%i dim:%i' % (img_len, img_wid, img_dim))
except:
    print('Error accessing Image. Check file type')
