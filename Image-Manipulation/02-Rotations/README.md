

# Python OpenCV – Rotation

 ## `cv2.rotate()` Method

`cv2.rotate()` method is used to rotate a 2D array in multiples of 90 degrees. The function cv::rotate rotates the array in three different ways.

  

```
Syntax: cv2.cv.rotate( src, rotateCode[, dst] )
```

  
  



### Parameters:
 
> **<u>src</u>:** It is the image whose color space is to be changed.
> 
> **<u>rotateCode</u>:** It is an enum to specify how to rotate the array.
> 
> **<u>dst</u>:** It is the output image of the same size and depth as src image.
> It is an optional parameter.
> 
>   
> 
> **<u>Return Value</u>:** It returns an image.


  

There are three arguments to choose from, for the rotateCode parameter:

  

-  **Rotate the image by 90:** rotateCode = `ROTATE_90_CLOCKWISE`.

-  **Rotate the image by 180:** rotateCode = `ROTATE_180`.

-  **Rotate the image by 270:** rotateCode = `ROTATE_90_COUNTERCLOCKWISE`.


## `getRotationMatrix2D()` & `wrapAfine()` method

OpenCV provides the  `getRotationMatrix2D()`  function to create a transformation matrix.

The following is the syntax for creating the 2D rotation matrix:

```
getRotationMatrix2D(center, angle, scale)
```

The  `getRotationMatrix2D()`  function takes the following arguments:

-   `center`: the center of rotation for the input image
-   `angle`: the angle of rotation in degrees
-   `scale`: an isotropic scale factor which scales the image up or down according to the value provided

If the  `angle`  is positive, the image gets rotated in the counter-clockwise direction. If you want to rotate the image clockwise by the same amount, then the  `angle`  needs to be negative.

Rotation is a three-step operation:

1.  First, you need to get the center of rotation. This typically is the center of the image you are trying to rotate.
2.  Next, create the 2D-rotation matrix. OpenCV provides the  `getRotationMatrix2D()`  function that we discussed above.
3.  Finally, apply the affine transformation to the image, using the rotation matrix you created in the previous step. The  `warpAffine()`  function in OpenCV does the job.

The `warpAffine()` function applies an affine transformation to the image. After applying affine transformation, all the parallel lines in the original image will remain parallel in the output image as well.

### Example:
```
rotate_matrix = cv2.getRotationMatrix2D(center = center, angle = 45, scale = 1)
rotated_image = cv2.warpAffine(src = image, M = rotate_matrix, dsize = (width, height))