
# Python program to explain cv2.rotate() method
  
# importing cv2
import cv2
import numpy as np
from matplotlib import pyplot as plt
  
# path
path = 'Images\input.jpeg'
  
# Reading an image in default mode
src = cv2.imread(path)

# Using cv2.rotate() method
# Using cv2.ROTATE_90_CLOCKWISE rotate
# by 90 degrees clockwise
image_90 = cv2.rotate(src, cv2.cv2.ROTATE_90_CLOCKWISE)
image_180 = cv2.rotate(src, cv2.cv2.ROTATE_180)
image_270 = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title('Original')

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(image_90, cv2.COLOR_BGR2RGB))
plt.title('Clockwise 90 Rotation')
  
plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(image_180, cv2.COLOR_BGR2RGB))
plt.title('180 Rotation')

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(image_270, cv2.COLOR_BGR2RGB))
plt.title('270 Rotation')

plt.savefig('Images\output.png')
plt.show()
