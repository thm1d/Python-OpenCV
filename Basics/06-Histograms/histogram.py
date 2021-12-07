import cv2
from matplotlib import pyplot as plt
# load an image in grayscale mode
img = cv2.imread('Images\input4.jpg',0)
  
# calculate frequency of pixels in range 0-255
histg = cv2.calcHist([img],[0],None,[256],[0,256]) 

# show the plotting graph of an image
plt.plot(histg)
plt.savefig('Images\histogram_04.png')
plt.show()