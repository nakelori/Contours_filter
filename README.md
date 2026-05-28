An image filter to find and display the contours of the objects in the image. 
1. Convert the image to gray scale.
2. Convert it to a binary image.
3. Calculate a matrix convolution of the image with the kernel ([0,-1,0],[-1,4,-1],[0,-1,0]) and sum the result into the middle pixel.
4. Dispaly the contours image. Usefull to for object detection and finding objects in an image.
