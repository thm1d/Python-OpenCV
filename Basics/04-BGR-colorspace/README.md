# RGB Colorspace OpenCV
When the image file is read with the OpenCV function `imread()`, the order of colors is BGR (blue, green, red). 

RGB stands for Red Green Blue. Most often, an RGB color is stored in a structure or unsigned integer with Blue occupying the least significant "area" (a byte in 32-bit and 24-bit formats), Green the second least, and Red the third least.

BGR is the same, except the order of areas is reversed. Red occupies the least significant area, Green the second (still), and Blue the third.

## Colorspace Conversion
When reading a color image file, OpenCV `imread()` reads as a NumPy array `ndarray` of `row (height) x column (width) x color (3)`. The order of color is BGR (blue, green, red).

We can use cvtColor() method to convert a BGR image to RGB and vice-versa. The OpenCV function `imwrite()` that saves an image assumes that the order of colors is BGR, so it is saved as a correct image.

> **Syntax:** cv2.cvtColor(src, code)
> 
> **Parameter:**
> 
> -   **src:** It is the image whose color space is to be changed.  
> -    **code:** It is the color space conversion code.
>       - **cv2.COLOR_BGR2RGB** – BGR image is converted to RGB.
>       - **cv2.COLOR_RGB2BGR** – RGB image is converted to BGR.

Converting a BGR image to RGB and vice versa can have several reasons, one of them being that several image processing libraries have different pixel orderings.