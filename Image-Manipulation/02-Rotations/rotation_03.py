import cv2
import numpy as np
from matplotlib import pyplot as plt

#Other Option to Rotate
img = cv2.imread('Images/input.jpeg')

rotated_image = cv2.transpose(img)

plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
plt.title('Rotated Image - Method 2')

plt.savefig(r'Images\rotation_with_transpose.png')
plt.show()

# Let's now to a horizontal flip.
flipped = cv2.flip(img, 1)

plt.imshow(cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB))
plt.title('Horizontal Flip')

plt.savefig(r'Images\rotation_with_flip.png')
plt.show()