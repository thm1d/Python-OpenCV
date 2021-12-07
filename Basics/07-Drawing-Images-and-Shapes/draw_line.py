import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(r'Images\black.jpg')

# cv.line(image, p0, p1, color, thickness)
# Draw a diagonal blue line of thickness of 5 pixels
image = np.zeros((512,512,3), np.uint8)
cv2.line(image, (0,511), (511,0), (255,127,0), 50)
cv2.line(image, (0,0), (511,511), (255,127,0), 50)
 
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Bule Linear line')

plt.savefig('Images\output_line.png')
plt.show()