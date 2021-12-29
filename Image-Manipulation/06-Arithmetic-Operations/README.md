
## Goal

-   Learn several arithmetic operations on images, like addition, subtraction, bitwise operations, and etc.
-   Learn these functions:  `cv.add()`,  `cv.addWeighted()`, etc.

## Image Addition

You can add two images with the OpenCV function,  `cv.add()`, or simply by the numpy operation `res = img1 + img2`. Both images should be of same depth and type, or the second image can just be a scalar value.

### Note

There is a difference between OpenCV addition and Numpy addition. OpenCV addition is a saturated operation while Numpy addition is a modulo operation.

For example, consider the below sample:
```
x = np.uint8([250])

y = np.uint8([10])

print( cv.add(x,y) ) # 250+10 = 260 => 255
[[255]]

print( x+y ) # 250+10 = 260 % 256 = 4
[4]
```
This will be more visible when you add two images. Stick with OpenCV functions, because they will provide a better result.

## Image Blending

This is also image addition, but different weights are given to images in order to give a feeling of blending or transparency. Images are added as per the equation below:
<center>
g(x)=(1−α)f0(x)+αf1(x)
</center>
By varying  α  from  0→1, you can perform a cool transition between one image to another.

Here I took two images to blend together. The first image is given a weight of 0.7 and the second image is given 0.3. ` cv.addWeighted()` applies the following equation to the image:
<center>
dst=α⋅img1+β⋅img2+γ
</center>
Here  γ  is taken as zero.

```
img1 = cv.imread('ml.png')
img2 = cv.imread('opencv-logo.png')

dst = cv.addWeighted(img1,0.7,img2,0.3,0)

cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
 ```

## Addition of Image:

We can add two images by using function  `cv2.add()`. This directly adds up image pixels in the two images.  

```
Syntax: cv2.add(img1, img2)
```

But adding the pixels is not an ideal situation. So, we use `cv2.addweighted()`. Remember, both images should be of equal size and depth.  

> **Syntax**: cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)  
> 
> **Parameters**:  
> 
> **img1**: First Input Image array(Single-channel, 8-bit or floating-point)  
> 
> **wt1**: Weight of the first input image elements to be applied to the final image  
> 
> **img2**: Second Input Image array(Single-channel, 8-bit or floating-point)  
> 
> **wt2**: Weight of the second input image elements to be applied to the final image  
> 
> **gammaValue**: Measurement of light

## Subtraction of Image:

Just like addition, we can subtract the pixel values in two images and merge them with the help of cv2.subtract(). The images should be of equal size and depth.  

```
Syntax:  cv2.subtract(src1, src2)
```