import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(r'Images\black.jpg')

image = np.zeros((512,512,3), np.uint8)

# cv2.cirlce(image, center, radius, color, fill)
cv2.circle(image, (256, 256), 100, (15,75,50), 50) 

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Circle')

plt.savefig('Images\output_circle.png')
plt.show()