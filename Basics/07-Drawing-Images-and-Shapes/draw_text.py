import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(r'Images\black.jpg')

image = np.zeros((512,512,3), np.uint8)

# cv2.putText(image, 'Text to Display', bottom left starting point, Font, Font Size, Color, Thickness)
cv2.putText(image, 'I love Computer Vision', (75,290), cv2.FONT_HERSHEY_COMPLEX, 1, (100,170,0), 3)  
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('I love Computer vision')

plt.savefig('Images\output_text.png')
plt.show()