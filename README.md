# segmentation_tool
## A color segmentation tool to find HSV ranges to reach a desired mask in OpenCV

* This project is a simple script written in Python using OpenCV to help in the task of finding optimal HSV ranges in the color segmentation process
* It currently features: <br>
    1. A HSV window that simply shows the webcam image in the HSV colorspace
    2. Individual windows showing Hue, Saturation and Value images
    5. A window featuring trackbars in order to adjust the segmentation parameters
    6. A window that shows the mask applied with the selected aparameters
    7. If the HSV window is clicked, the program prints out the HSV values for that pixel
    
* This project depends on:
  - OpenCV
  - Numpy
  
* To-do: <br>
  - [ ] A window that shows a colored square with the color of the selecte pixel, as well as its values
