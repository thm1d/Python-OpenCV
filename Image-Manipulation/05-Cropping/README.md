## Cropping Using OpenCV

In Python, you crop the image using the same method as NumPy array slicing. To slice an array, you need to specify the start and end index of the first as well as the second dimension.

  

The first dimension is always the number of rows or the height of the image.

The second dimension is the number of columns or the width of the image.

It goes with the convention that the first dimension of a 2D array represents the rows of the array (where each row represents the y-coordinate of the image). How to slice a NumPy array? Check out the syntax in this example:

  
```
cropped = img[start_row:end_row, start_col:end_col]
```