import cv2 as cv
import numpy as np
import PIL
from PIL import Image


img= Image.open('C:\\Users\\Shuaib Feroze\\Documents\\Kaggle hand gesture recognition\\leapGestRecog\\02\\03_fist\\frame_02_03_0001.png').convert('L')
img = np.array(img)
print(img)
print(img.shape)


# img = cv.imread('C:\\Users\\Shuaib Feroze\\Documents\\Kaggle hand gesture recognition\\leapGestRecog\\02\\03_fist\\frame_02_03_0001.png')
# cv.imshow('frame',img)
# cv.waitKey(0)
# print(img)
# print(img.shape)