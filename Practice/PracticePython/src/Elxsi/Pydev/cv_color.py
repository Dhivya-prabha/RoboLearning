import cv2 
   
# path 
path = r'D:/Practice/PracticePython/img1/soccer.jpg'
   
# Reading an image in default mode
src = cv2.imread(path)
   
# Window name in which image is displayed
window_name = 'Image'  
# Using cv2.cvtColor() method
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )
#image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV )  
# Displaying the image 
cv2.imshow(window_name, image)
cv2.waitKey(2000)

