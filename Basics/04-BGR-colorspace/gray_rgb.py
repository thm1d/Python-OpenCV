import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('Images\input1.jpg')

# BGR Values for the first 0,0 pixel
B, G, R = image[0, 0] 
print (B, G, R)
print (image.shape)

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print (gray_img.shape)
print (gray_img[0, 0]) 

# OpenCV's 'split' function splites the image into each color index
B, G, R = cv2.split(image)
cv2.imshow('Blue in BGR', B)
print (B.shape)

row, col = 1, 3
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()
 
axs[0].imshow(cv2.cvtColor(R, cv2.COLOR_BGR2RGB))
axs[0].set_title('Red')

axs[1].imshow(cv2.cvtColor(G, cv2.COLOR_BGR2RGB))
axs[1].set_title('Green')

axs[2].imshow(cv2.cvtColor(B, cv2.COLOR_BGR2RGB))
axs[2].set_title('Blue')

plt.show()

row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()
 
merged = cv2.merge([B, G, R]) 
axs[0].imshow(cv2.cvtColor(merged, cv2.COLOR_BGR2RGB))
axs[0].set_title('Merged')

merged_with_blue_amplified = cv2.merge([B+100, G, R])
axs[1].imshow(cv2.cvtColor(merged_with_blue_amplified, cv2.COLOR_BGR2RGB))
axs[1].set_title('Merged with Blue Amplified')

plt.show()

# use 'imwrite' specificing the file name and the image to be saved
cv2.imwrite('Images\merged_bgr.jpg', merged)
cv2.imwrite('Images\merged_with_blue_amplified.jpg', merged_with_blue_amplified)
cv2.imwrite('Images\merged_with_blue_amplified.png', merged_with_blue_amplified)