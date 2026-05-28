import cv2
import numpy as np


imgn = cv2.imread('face.jpg') #insert the image name file
img1 = cv2.resize(imgn,(int(imgn.shape[1]*3),int(imgn.shape[0]*3))) #resize if needed
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) #convert to gray scale
contours = np.empty((img1.shape[0]-2, img1.shape[1]-2)) 

ret, B = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY) #convert to binary
A=  np.array([[0,-1,0],[-1,4,-1],[0,-1,0]]) #define the kernel
print(B.shape)

for i in range(img1.shape[0]-2):
    for j in range( img1.shape[1]-2):
        contours[i][j]  = np.sum(B[i:i+3,j:j+3]*A) #convolotion

contours = np.uint8(np.absolute(contours)) #convert contours image to np array
cv2.imshow('open',img1)
cv2.imshow('opens',contours)
cv2.waitKey(0)

        