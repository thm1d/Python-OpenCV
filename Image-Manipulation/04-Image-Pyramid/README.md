
# Image Pyramid using OpenCV

An “image pyramid” is a  **_multi-scale representation_**  of an image.

Utilizing an image pyramid allows us to  **find objects in images at different scales**  of an image. And when combined with a  **sliding window**  we can find objects in images in various locations.

The `pyrUp()` function increases the size to double of its original size and `pyrDown()` function decreases the size to half. If we keep the original image as a base image and go on applying `pyrDown` function on it and keep the images in a vertical stack, it will look like a pyramid. The same is true for upscaling the original image by `pyrUp` function.

![](https://pyimagesearch.com/wp-content/uploads/2015/03/pyramid_example.png)

## Pyramid Up

In Pyramid Up, the image is initially up-sampled and then blurred. You can perform Pyramid Up operation on an image using the  `pyrUP()`  method of the  `imgproc`  class. Following is the syntax of this method −

```
pyrUp(src, dst, dstsize, borderType)
```

## Pyramid Down

In Pyramid Down, the image is initially blurred and then down-sampled. You can perform Pyramid Down operation on an image using the  `pyrDown()`  method of the  `imgproc`  class. Following is the syntax of this method −

```
pyrDown(src, dst, dstsize, borderType)
```

