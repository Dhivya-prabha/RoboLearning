import cv2
import numpy as np
from matplotlib import pyplot as plt
  
# reading the input image
img = cv2.imread('D:/Practice/PracticePython/img1/soccer.jpg')
  
# define colors to plot the histograms
colors = ('b','g','r')
  
# compute and plot the image histograms
for i,color in enumerate(colors):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color = color)
plt.title('soccer GFG')
plt.show()