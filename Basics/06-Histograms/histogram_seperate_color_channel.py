import cv2
from matplotlib import pyplot as plt

image = cv2.imread('Images\input4.jpg')
# Viewing Separate Color Channels
color = ('b', 'g', 'r')

# We now separate the colors and plot each in the Histogram
for i, col in enumerate(color):
    histogram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram2, color = col)
    plt.xlim([0,256])

plt.savefig('Images\histogram_seperate_color_04.png')
plt.show()