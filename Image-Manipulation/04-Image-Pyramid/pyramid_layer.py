import cv2
import matplotlib.pyplot as plt
  
img = cv2.imread("Images/input1.jpg")

layer = img.copy()
  
for i in range(7):
    plt.subplot(3, 3, i + 1)

    if(i<4):  
        # using pyrDown() function
        layer = cv2.pyrDown(layer)
    
        plt.imshow(layer)
        cv2.imshow("str(i)", layer)
    else:  
        # using pyrUp() function
        layer = cv2.pyrUp(layer)
    
        plt.imshow(layer)
        cv2.imshow("str(i)", layer)
    cv2.waitKey(0)
      
  
cv2.destroyAllWindows()