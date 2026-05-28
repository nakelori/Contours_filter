An image filter to find and display the contours of the objects in the image. Usefull for object detection and finding objects in an image.
1. Convert the image to gray scale.
2. Convert it to a binary image.
3. Calculate a matrix convolution of the image with the laplace kernel ([0,-1,0],[-1,4,-1],[0,-1,0]) and sum the result into the middle pixel.
what it means is we slide the kernel over the whole image pixel by pixel and for each pixel we do a dot product multiplication. the sum of those 9 multiplications will be the value of the middle of this 3X3 area. the kernel can give a result of 0 or +-1. if it's 0 it means the surface is uniform. other wise we have a contour and the value in the outcome of the pixel will be 1.
4. notice that the frame of the whole image is being cut by 1 pixel at each side. it means that if the original picture was 100X100 pixels now it's 98X98 pixels. to solve this you can handle a smaller image or assume the value that shouldv'e been on the edges and recalculate them and add.
5. Dispaly the contours image.

