# Drawing images and shapes using OpenCV

OpenCV provides many drawing functions to draw geometric shapes and write text on images. Let’s see some of the drawing functions and draw geometric shapes on images using OpenCV.

Some of the drawing functions are :

`cv2.line()` : Used to draw line on an image. 

`cv2.rectangle()` : Used to draw rectangle on an image. 

`cv2.circle()`s : Used to draw circle on an image. 

`cv2.putText()` : Used to write text on image.

## Draw a line
The function cv.line() adds a line to an image:

```
cv.line(image, p0, p1, color, thickness)
```
- **image** where the line is added
- start point **p0**
- end point **p1**
- line **color**
- line **thickness**

## Draw a rectangle
The function cv.rectangle() adds a rectangle to an image:

```
cv.rectangle(image, p0, p1, color, thickness)
```
- **image** where the rectangle is added
- corner point **p0**
- corner point **p1**
- ouline **color**
- line **thickness**

If the line thickness is negative or `cv.FILLED` the rectangle is filled:

```
cv.rectangle(img, p0, p1, BLUE, 2)
cv.rectangle(img, p2, p3, GREEN, cv.FILLED)
```

## Draw an ellipse
The function `cv.ellipes()` adds an ellipse to an image:

```
cv.ellipse(img, center, axes, angle, a0, a1, color, thickness)
```
- **image** where the ellipse is added
- **center** point
- the two **axes**
- the axis orientation **angle**
- the beginning angle **a0**
- the ending angle **a1**
- ouline **color**
- line **thickness**

## Draw a polygon
The `polylines` function expects a Numpy array for the point list:

```
pts = [(50, 50), (300, 190), (400, 10)]
cv.polylines(img, np.array([pts]), True, RED, 5)
```

## Draw text
`cv2.putText()` method is used to draw a text string on any image.

```
cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
```

- **image:** It is the image on which text is to be drawn.
- **text:** Text string to be drawn.
- **org:** It is the coordinates of the bottom-left corner of the text string in the image. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).
- **font:** It denotes the font type. Some of font types are `FONT_HERSHEY_SIMPLEX`, `FONT_HERSHEY_PLAIN`, , etc.
- **fontScale:** Font scale factor that is multiplied by the font-specific base size.
- **color:** It is the color of text string to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
- **thickness:** It is the thickness of the line in px.
- **lineType:** This is an optional parameter.It gives the type of the line to be used.
- **bottomLeftOrigin:** This is an optional parameter. When it is true, the image data origin is at the bottom-left corner. Otherwise, it is at the top-left corner.



- **Return Value:** It returns an image.
