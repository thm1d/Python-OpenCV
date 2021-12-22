import cv2
import numpy as np

img = cv2.imread('Images\input3.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(len(img))
print(len(img[0]))

print(img.shape)
print(img[0][0])

for i in range(img.shape[0]):
    for j in  range(0, 20):
        img[i][j] = 0
    
    for j in  range(img.shape[1] - 20, img.shape[1]):
        img[i][j] = 0

for j in range(img.shape[1]):
    for i in  range(0, 20):
        img[i][j] = 0
    
    for i in  range(img.shape[0] - 20, img.shape[0]):
        img[i][j] = 0
        

cv2.imshow('image',img)
cv2.waitKey(0) 

