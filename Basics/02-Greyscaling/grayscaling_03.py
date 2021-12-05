import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load our input image
image = cv2.imread('Images\input3.jpg')

# We use cvtColor, to convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()
 
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original')

axs[1].imshow(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB))
axs[1].set_title('Grayscale')

plt.show()

# use 'imwrite' specificing the file name and the image to be saved
cv2.imwrite('Images\output_03.jpg', gray_image)
cv2.imwrite('Images\output_03.png', gray_image)