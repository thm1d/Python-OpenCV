# Method 1: Using the cv2.cvtColor() function


# import opencv
import cv2
 
# Load the input image
image = cv2.imread('images\input.jpg')
cv2.imshow('Original', image)
 
# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0) 
 
# Window shown waits for any key pressing event
cv2.destroyAllWindows()

cv2.imwrite('images\output_01.jpg', gray_image)