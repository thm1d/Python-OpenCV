
# Grayscaling

#### Grayscaling is process by which an image is converted from a full color to shades of grey (black & white). It varies between complete black and complete white.

In OpenCV, many functions grayscale images before processing. This is done because it simplifies the image, acting almost as a noise reduction and increasing processing time as there is less information in the image.

  

## Importance of Grayscaling

- <strong>Dimension reduction:</strong> For example, In RGB images there are three color channels and has three dimensions while grayscale images are single-dimensional.

- <strong>Reduces model complexity:</strong> Consider training neural article on RGB images of 10x10x3 pixel. The input layer will have 300 input nodes. On the other hand, the same neural network will need only 100 input nodes for grayscale images.

- <strong>For other algorithms to work:</strong> Many algorithms are customized to work only on grayscale images e.g. Canny edge detection function pre-implemented in OpenCV library works on Grayscale images only.