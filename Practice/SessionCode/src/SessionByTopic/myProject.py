import cv2
import os
import glob
import numpy as np
  
  
imdir = 'D:/Practice/PracticePython/img'
images = []
name =[]
for img in glob.glob("D:/Practice/PracticePython/img/*.jpg"):
    n= cv2.imread(img)
    images.append(n)
    name.append(img)
# test image
image = cv2.imread('D:/Practice/PracticePython/img1/soccer.jpg')
# cv2.COLOR_BGR2GRAY color space for convert an image from one color space to another
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#calcHist calculate the image histograms
test = cv2.calcHist([gray_image], [0],
                         None, [256], [0, 256])
   
i =0
histogram = []
for m in glob.glob("D:/Practice/PracticePython/img/*.jpg"):
    n= cv2.imread(m)
    i+= 1
    gray_image = cv2.cvtColor(n, cv2.COLOR_BGR2GRAY)
    histogram.append(cv2.calcHist([gray_image], [0],
                          None, [256], [0, 256]))

c1 = []
#Calculate the Euclidean distance between images using NumPy
for a in histogram:
    i = 0 
    c = 0   
    while i<len(test) and i<len(a):
        c+=(test[i]-a[i])**2
        i+= 1
    c1.append(c**(1 / 2))
inImage = name[c1.index(min(c1))].split("\\")
print('More similar image to soccer is ',inImage[-1])
    
   
    
    
    
    
    
    
    
    
    
    