
# Read, Display and Write an Image using OpenCV

Reading, displaying, and writing images are basic to image processing and computer vision. Even when cropping, resizing, rotating, or applying different filters to process images, you’ll need to first read in the images. So it’s important that you master these basic operations.


OpenCV has these three built-in functions :


- `imread()` helps us read an image
- `imshow()` displays an image in a window
- `imwrite()` writes an image into the file directory


## Reading an Image

For reading an image, use the imread() function in OpenCV. Here’s the syntax:


`imread(filename, flags)`


It takes two arguments:


1) The first argument is the image name, which requires a fully qualified pathname to the file.

2) The second argument is an optional flag that lets you specify how the image should be represented. OpenCV offers several options for this flag, but those that are most common include:

- cv2.IMREAD_UNCHANGED or -1
- cv2.IMREAD_GRAYSCALE or 0
- cv2.IMREAD_COLOR or 1


## Displaying an Image

In OpenCV, you display an image using the imshow() function. Here’s the syntax:


`imshow(window_name, image)`


This function also takes two arguments:


- The first argument is the window name that will be displayed on the window.

- The second argument is the image that you want to display.


## Writing an Image

Finally, let’s discuss how to write/save an image into the file directory, using the imwrite() function. Check out its syntax:


`imwrite(filename, image).`


- The first argument is the filename, which must include the filename extension (for example .png, .jpg etc). OpenCV uses this filename extension to specify the format of the file.

- The second argument is the image you want to save. The function returns True if the image is saved successfully.