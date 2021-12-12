import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Images\input1.jpg', 1)
# Loading the image

width = image.shape[1]
height = image.shape[0]

print(image.shape)
print(width, height)

half = cv2.resize(image, (640, 393), fx = 0.1, fy = 0.1)
bigger = cv2.resize(image, (1600, 1000))

stretch_near = cv2.resize(image, (1300, 750),
			interpolation = cv2.INTER_NEAREST)


Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[image, half, bigger, stretch_near]
count = 4

for i in range(count):
	plt.subplot(2, 2, i + 1)
	plt.title(Titles[i])
	plt.imshow(images[i])

plt.savefig('Images\output_01.png')
plt.show()
