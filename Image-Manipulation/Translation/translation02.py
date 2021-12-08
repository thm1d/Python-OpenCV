import cv2
import numpy as np
from matplotlib import pyplot as plt

import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('Images\input3.jpg')

# Store height and width of the image
height, width = image.shape[:2]

quarter_height, quarter_width = height/4, width/4
print ("height.shape: ", height)
print ("quarter_height.shape: ", quarter_height)

print ("width.shape: ", width)
print ("quarter_width.shape: ", quarter_width)

#       | 1 0 Tx |
#  T  = | 0 1 Ty |
# T is our translation matrix
T = np.float32([[1, 0, quarter_width], 
                [0, 1,quarter_height]])

# Let's take a look at T
print (T)

# We use warpAffine to transform the image using the matrix, T
img_translation = cv2.warpAffine(image, T, (width, height))
print (img_translation.shape)

plt.imshow(cv2.cvtColor(img_translation, cv2.COLOR_BGR2RGB))
plt.title('Translation Quarter Shift')

plt.savefig('Images\output_quarter_shift_03.png')
plt.show()

half_height, half_width = height/2, width/2
print ("quarter_height.shape: ", half_height)
print ("quarter_width.shape: ", half_width)

T = np.float32([[1, 0, half_height], 
                [0, 1,half_width]])

# Let's take a look at T
print (T)

# We use warpAffine to transform the image using the matrix, T
img_translation = cv2.warpAffine(image, T, (width, height))
print (img_translation.shape)

plt.imshow(cv2.cvtColor(img_translation, cv2.COLOR_BGR2RGB))
plt.title('Translation Half Shift')

plt.savefig('Images\output_half_shift_03.png')
plt.show()