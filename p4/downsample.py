import cv2
import numpy as np


orgImg = cv2.imread('Goldhill.bmp')


kernel = np.ones((5,5),np.float32)/25
avgImage = cv2.filter2D(orgImg,-1,kernel)


cv2.imshow('originalImage' , orgImg)
cv2.imshow('averageImage' , avgImage)
cv2.waitKey(0)
