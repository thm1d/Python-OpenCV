import cv2
import numpy as np

frame = cv2.imread('Images\input5.jpg')

# Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Blue -> [120, 255, 255]
# define range of blue color in HSV.  You can take [H-20, 100,100] and [H+20, 255, 255] as lower bound and upper bound respectively

lower_blue = np.array([100,100,100])
upper_blue = np.array([140,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame,frame, mask= mask)

cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('Images\output_05.jpg', res)
cv2.imwrite('Images\mask.jpg', mask)
