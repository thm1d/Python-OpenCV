import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('Images/input1.jpg')

B, G, R = cv2.split(image)

# Let's create a matrix of zeros 
# with dimensions of the image h x w  
zeros = np.zeros(image.shape[:2], dtype = "uint8")

row, col = 2, 3
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()
 
axs[0][0].imshow(cv2.merge([R, zeros, zeros]) )
axs[0][0].set_title('Red')

axs[0][1].imshow(cv2.merge([zeros, G, zeros]))
axs[0][1].set_title('Green')

axs[0][2].imshow(cv2.merge([zeros, zeros, B]))
axs[0][2].set_title('Blue')

axs[1][0].imshow(cv2.merge([R, G, B]))
axs[1][0].set_title('RGB Merged')

axs[1][1].imshow(cv2.merge([B, G, R]))
axs[1][1].set_title('BGR Merged')

axs[1][2].imshow(cv2.merge([G, B, R]))
axs[1][2].set_title('GBR Merged')


plt.show()

cv2.imwrite('Images\output_red.jpg', cv2.merge([R, zeros, zeros]))
cv2.imwrite('Images\output_green.jpg', cv2.merge([zeros, G, zeros]))
cv2.imwrite('Images\output_blue.jpg', cv2.merge([zeros, zeros, B]))

cv2.imwrite('Images\RGB_merger.jpg', cv2.merge([R, G, B]))
cv2.imwrite('Images\BGR_merger.jpg', cv2.merge([B, G, R]))
cv2.imwrite('Images\GBR_merger.jpg', cv2.merge([G, B, R]))