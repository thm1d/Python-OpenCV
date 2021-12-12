import cv2
 
img = cv2.imread('Images/input1.jpg', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
width = 1800
height = img.shape[0] # keep original height
dim = (width, height)
 
# resize image
resized_width = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized_width.shape)
 
cv2.imshow("Width Resized image", resized_width)
cv2.imwrite(r'Images\resized_width_01.jpg',resized_width)

width = img.shape[1]
height = 1000 # keep original height
dim = (width, height)
 
# resize image
resized_height = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized_height.shape)
 
cv2.imshow("Height Resized image", resized_height)
cv2.imwrite(r'Images\resized_height_01.jpg',resized_height)

width = 1920
height = 1080 # keep original height
dim = (width, height)
 
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Height & Width Resized Dimensions : ',resized.shape)
 
cv2.imshow("Height & Width Resized image", resized)
cv2.imwrite(r'Images\resized_height_width_01.jpg',resized)

cv2.waitKey(0)
cv2.destroyAllWindows()