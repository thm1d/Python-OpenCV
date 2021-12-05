# Method 2: Using the cv2.imread() function with flag = zero


# Import opencv
import cv2
 
# Use the second argument or (flag value) zero
# that specifies the image is to be read in grayscale mode
img = cv2.imread('images\input2.jpg', 0)
 
cv2.imshow('Grayscale Image', img)
cv2.waitKey(0)
 
# Window shown waits for any key pressing event
cv2.destroyAllWindows()

cv2.imwrite('images/output_02.jpg', img)