import cv2
import glob
import numpy as np


imdir = 'D:/Practice/PracticePython/img'
images = []
name =[]
for img in glob.glob("D:/Practice/PracticePython/img/*.jpg"):
    n= cv2.imread(img)
    images.append(n)
    name.append(img)
print(name)
