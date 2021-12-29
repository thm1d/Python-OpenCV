import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('Images/input3.jpg')

# Create a matrix of ones, then multiply it by a scaler of 100 
# This gives a matrix with same dimesions of our image with all values being 100
M = np.ones(image.shape, dtype = "uint8") * 100 
row, col = 1, 3
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()

axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')
cv2.imwrite('image.png', image)
 
# We use this to add this matrix M, to our image
# Notice the increase in brightness
added = cv2.add(image, M)
axs[1].imshow(cv2.cvtColor(added, cv2.COLOR_BGR2RGB))
axs[1].set_title('Added Image')
cv2.imwrite('Added_image.png', added)

# Likewise we can also subtract
# Notice the decrease in brightness
subtracted = cv2.subtract(image, M)
axs[2].imshow(cv2.cvtColor(subtracted, cv2.COLOR_BGR2RGB))
axs[2].set_title('Subtracted')
cv2.imwrite('subtracted_image.png', subtracted)

plt.savefig('Images\output.png')
plt.show()
