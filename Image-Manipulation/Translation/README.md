
# Translation

  

Translation is the shifting of an image along the x- and y-axis.

To translate an image using OpenCV, we must:

  

- Load an image from disk

- Define an affine transformation matrix

- Apply the `cv2.warpAffine` function to perform the translation

  

## OpenCV Image Translation

  

### Defining a translation matrix with OpenCV

  

To perform image translation with OpenCV, we first need to define a 2 x 3 matrix called an **affine transformation matrix**:

  

<center><img src="https://929687.smushcdn.com/2407837/wp-content/uploads/2021/01/opencv_translate_matrix.png?lossy=1&strip=1&webp=1"/></center>


To translate an image with OpenCV, we must first construct an affine transformation matrix.

For the purposes of translation, all we care about are the t_{x} and t_y values:

  

- Negative values for the t_{x} value will shift the image to the left

- Positive values for t_{x} shifts the image to the right

- Negative values for t_{y} shifts the image up

- Positive values for t_{y} will shift the image down

For example, let’s suppose we want to shift an image 25 pixels to the  _right_ and 50 pixels  _down_. Our translation matrix would look like the following (implemented as a NumPy array):

OpenCV Image Translation
```
M = np.float32([
[1, 0, 25],
[0, 1, 50]
])
```
Now, if we want to shift an image 7 pixels to the  _left_ and 23 pixels  _up_, our translation matrix would look like the following:

OpenCV Image Translation
```
M = np.float32([
[1, 0, -7],
[0, 1, -23]
])
```
And as a final example, let’s suppose we want to translate our image 30 pixels to the  _left_ and 12 pixels  _down_:

OpenCV Image Translation
```
M = np.float32([
[1, 0, -30],
[0, 1, 12]
])
```
Once our transformation matrix is defined, we can simply perform the image translation using the `cv2.warpAffine` function, like so:

OpenCV Image Translation
```
cv2.warpAffine(src, M, dsize, dst, flags, borderMode, borderValue)
```

**Parameters**:

**src**: input image.
**dst**: output image that has the size dsize and the same type as src.
**M**: transformation matrix.
**dsize**: size of the output image.
**flags**: combination of interpolation methods (see resize() ) and the optional flag
`WARP_INVERSE_MAP` that means that M is the inverse transformation (dst->src).
**borderMode**: pixel extrapolation method; when `borderMode=BORDER_TRANSPARENT`, it means that the pixels in the destination image corresponding to the “outliers” in the source image are not modified by the function.
**borderValue**: value used in case of a constant border; by default, it is 0.

**Example**:
```
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
```