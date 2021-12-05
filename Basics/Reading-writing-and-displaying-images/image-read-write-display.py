import cv2

# Read an image

img_color = cv2.imread('input.jpg',cv2.IMREAD_COLOR)
img_grayscale = cv2.imread('input.jpg',cv2.IMREAD_GRAYSCALE)
img_unchanged = cv2.imread('input.jpg',cv2.IMREAD_UNCHANGED)

# or
# img_color = cv2.imread('input.jpg',1)
# img_grayscale = cv2.imread('input.jpg',0)
# img_unchanged = cv2.imread('input.jpg',-1)


# Displays image inside a window

cv2.imshow('color image',img_color) 
cv2.imshow('grayscale image',img_grayscale)
cv2.imshow('unchanged image',img_unchanged)
 
# Waits for a keystroke

cv2.waitKey(0) 

# Destroys all the windows created

cv2.destroyAllWindows()

# Writing an image

cv2.imwrite('grayscale.jpg',img_grayscale)



