import cv2
 
img = cv2.imread('Images\input1.jpg', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)

cv2.imshow("Original Image", img)

scale_percent = 40 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)

cv2.imshow("Resized image", resized)
cv2.imwrite('Images\output_resized_40_01.jpg', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()