import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Images/input3.jpg')

smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(smaller)

row, col = 1, 3
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()
 
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')
cv2.imwrite('Images\original_image.png', image)

axs[1].imshow(cv2.cvtColor(smaller, cv2.COLOR_BGR2RGB))
axs[1].set_title('Smaller Image')
cv2.imwrite('Images\smaller_image.png', smaller)

axs[2].imshow(cv2.cvtColor(larger, cv2.COLOR_BGR2RGB))
axs[2].set_title('Larger Image')
cv2.imwrite('Images\larger_image.png', larger)

plt.show()

newer_image = cv2.imread('Images\larger_image.png')

new_smaller = cv2.pyrDown(newer_image)
new_larger = cv2.pyrUp(new_smaller)

row, col = 1, 3
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()
 
axs[0].imshow(cv2.cvtColor(newer_image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Newer Image')
cv2.imwrite(r'Images\newer_original_image.png', image)

axs[1].imshow(cv2.cvtColor(new_smaller, cv2.COLOR_BGR2RGB))
axs[1].set_title('Newer Smaller Image')
cv2.imwrite(r'Images\newer_smaller_image.png', new_smaller)

axs[2].imshow(cv2.cvtColor(new_larger, cv2.COLOR_BGR2RGB))
axs[2].set_title('Newer Larger Image')
cv2.imwrite(r'Images\newer_larger_image.png', new_larger)

plt.show()