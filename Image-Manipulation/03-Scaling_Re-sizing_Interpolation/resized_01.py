import cv2
import numpy as np
from matplotlib import pyplot as plt
# load our input image
image = cv2.imread('Images/input4.jpg')
row, col = 1, 3
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()

# Let's make our image 3/4 of it's original size
image_scaled = cv2.resize(image, None, fx=0.15, fy=0.15)
axs[0].imshow(cv2.cvtColor(image_scaled, cv2.COLOR_BGR2RGB))
axs[0].set_title('Scaling - Linear Interpolation')

# Let's double the size of our image
img_scaled_v1 = cv2.resize(image, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
axs[1].imshow(cv2.cvtColor(img_scaled_v1, cv2.COLOR_BGR2RGB))
axs[1].set_title('Scaling - Cubic Interpolation')

# Let's skew the re-sizing by setting exact dimensions
img_scaled_v2 = cv2.resize(image, (900, 400), interpolation = cv2.INTER_AREA)
axs[2].imshow(cv2.cvtColor(img_scaled_v2, cv2.COLOR_BGR2RGB))
axs[2].set_title('Scaling - Skewed Size')

plt.savefig('Images\output_scaling.png')
plt.show()