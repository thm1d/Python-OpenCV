import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an image using 'imread' specifying the path to image
input = cv2.imread('input2.jpg')

# Our file 'input.jpg' is now loaded and stored in python 
# as a varaible we named 'image'

# To display our image variable, we use 'imshow'
# The first parameter will be title shown on image window
# The second parameter is the image varialbe
plt.imshow(cv2.cvtColor(input, cv2.COLOR_BGR2RGB))
plt.title('Hello World')

plt.show()

# dimensions of the mage

print (input.shape)

# print each dimension of the image

print ('Height of Image:', int(input.shape[0]), 'pixels')
print ('Width of Image: ', int(input.shape[1]), 'pixels')

# use 'imwrite' specificing the file name and the image to be saved

cv2.imwrite('output.jpg', input)
cv2.imwrite('output.png', input)