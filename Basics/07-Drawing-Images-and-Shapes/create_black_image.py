import cv2
import numpy as np
from matplotlib import pyplot as plt

# Create a black image
image = np.zeros((512,512,3), np.uint8)

cv2.imwrite(r'Images\black.jpg', image)

# Can we make this in black and white?
image_bw = np.zeros((512,512), np.uint8)

row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()
 
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original RGB Colors')

axs[1].imshow(cv2.cvtColor(image_bw, cv2.COLOR_BGR2RGB))
axs[1].set_title('Original RGB Colors')


plt.show()