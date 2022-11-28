import cv2
  
     
# test image
image = cv2.imread('D:/Practice/PracticePython/img1/soccer.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram = cv2.calcHist([gray_image], [0],
                         None, [256], [0, 256])
  
# data1 image
image = cv2.imread('D:/Practice/PracticePython/img/tennis.jpg')
gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram1 = cv2.calcHist([gray_image1], [0],
                          None, [256], [0, 256])
  
# data2 image
image = cv2.imread('D:/Practice/PracticePython/img/ball.jpg')
gray_image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
histogram2 = cv2.calcHist([gray_image2], [0],
                          None, [256], [0, 256])
  
  
c1, c2 = 0, 0
  
# Euclidean Distance between data1 and test
i = 0
while i<len(histogram) and i<len(histogram1):
    c1+=(histogram[i]-histogram1[i])**2
    i+= 1
c1 = c1**(1 / 2)
  
 
# Euclidean Distance between data2 and test
i = 0
while i<len(histogram) and i<len(histogram2):
    c2+=(histogram[i]-histogram2[i])**2
    i+= 1
c2 = c2**(1 / 2)

print(c1, c2)
if(c1<c2):
    print("tennis is more similar to soccer")
else:
    print("ball is more similar to soccer")