import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(r'Images\black.jpg')

# Draw a Rectangle in
image = np.zeros((512,512,3), np.uint8)

# cv2.rectangle(image, starting vertex, opposite vertex, color, thickness)
cv2.rectangle(image, (100,100), (300,250), (127,50,127), 50)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.title('Rectangle')


plt.savefig('Images\output_rectangle.png')
plt.show()