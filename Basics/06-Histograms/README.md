# OpenCV Image Histograms 

Histograms are prevalent in nearly every aspect of computer vision.

We use grayscale histograms for thresholding. We use histograms for white balancing. We use color histograms for object tracking in images, such as with the CamShift algorithm.

We use color histograms as features — include color histograms in multiple dimensions.

And in an abstract sense, we use histograms of image gradients to form the HOG and SIFT descriptors.

Even the extremely popular bag-of-visual-words representation used in image search engines and machine learning is a histogram as well!

And in all likelihood, I’m sure this is not the first time you have run across histograms in your studies.

## Why Are Histograms So Useful?

Because histograms capture the frequency distribution of a set of data. And it turns out that examining these frequency distributions is a very nice way to build simple image processing techniques … along with very powerful machine learning algorithms.

## What is an Image Histogram?

A histogram represents the distribution of pixel intensities (whether color or grayscale) in an image. It can be visualized as a graph (or plot) that gives a high-level intuition of the intensity (pixel value) distribution. We are going to assume a RGB color space in this example, so these pixel values will be in the range of 0 to 255.

When plotting the histogram, the x-axis serves as our “bins.” If we construct a histogram with 256 bins, then we are effectively counting the number of times each pixel value occurs.

In contrast, if we use only 2 (equally spaced) bins, then we are counting the number of times a pixel is in the range [0, 128] or [128, 255].

The number of pixels binned to the x-axis value is then plotted on the y-axis.

## Using OpenCV to Compute Histograms with the `cv2.calcHist` Function

Here, we use cv2.calcHist()(in-built function in OpenCV) to find the histogram.

`cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])`

**images :** it is the source image of type uint8 or float32 represented as “[img]”.
**channels :** it is the index of channel for which we calculate histogram. For grayscale image, its value is [0] and
color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
**mask :** mask image. To find histogram of full image, it is given as “None”.
**histSize :** this represents our BIN count. For full scale, we pass [256].
**ranges :** this is our RANGE. Normally, it is [0,256].