
# OpenCV Python – Resize image

Resizing an image means changing the dimensions of it, be it width alone, height alone or changing both of them. Also, the aspect ratio of the original image could be preserved in the resized image. To resize an image, OpenCV provides cv2.resize() function.

In this tutorial, we shall the syntax of cv2.resize and get hands-on with examples provided for most of the scenarios encountered in regular usage.

## Syntax – cv2.resize()

The syntax of resize function in OpenCV is

`cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])`

## Parameter

  

**src** :[required] source/input image

**dsize** : [required] desired size for the output image

**fx** : [optional] scale factor along the horizontal axis

**fy** : [optional] scale factor along the vertical axis

**interpolation** : [optional] flag that takes one of the following methods.

-  `INTER_NEAREST`: a nearest-neighbor interpolation

-  `INTER_LINEAR`: a bilinear interpolation (used by default)

-  `INTER_AREA`: resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.

-  `INTER_CUBIC`: a bicubic interpolation over 4×4 pixel neighborhood INTER_LANCZOS4 – a Lanczos interpolation over 8×8 pixel neighborhood
```