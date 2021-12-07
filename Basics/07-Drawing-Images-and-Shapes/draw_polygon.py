import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(r'Images\black.jpg')

image = np.zeros((512,512,3), np.uint8)

# Let's define four points
pts = np.array( [[10,50], [400,50], [90,200], [50,500]], np.int32)

# Let's now reshape our points in form  required by polylines
pts = pts.reshape((-1,1,2))

cv2.polylines(image, [pts], True, (0,0,255), 30)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Polygon')

plt.savefig('Images\output_polygon.png')
plt.show()