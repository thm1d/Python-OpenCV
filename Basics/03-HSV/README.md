
# HSV

  

HSV is a color space that has three components: hue, saturation and value. When implementing object tracking based on color, images are often converted from RGB to HSV color space. Using HSV is much easier to represent a color and extract a colored object from an image than using RGB color space.

  

## What is HSV color space?

  

The HSV color space represents colors using three values

  

- <b>Hue :</b> This channel encodes color color information. Hue can be thought of an angle where 0 degree corresponds to the red color, 120 degrees corresponds to the green color, and 240 degrees corresponds to the blue color.

- <b>Saturation :</b> This channel encodes the intensity/purity of color. For example, pink is less saturated than red.

- <b>Value :</b> This channel encodes the brightness of color. Shading and gloss components of an image appear in this channel.

  

## Note

  

For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]. Different softwares use different scales. So if you are comparing OpenCV values with them, you need to normalize these ranges.