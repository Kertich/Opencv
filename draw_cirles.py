import numpy as np 
from cv2 import cv2 

# define a canvas of size 300*300 px, with 3 channels (R,G,B) and data type as 8 bit unsigned integer
canvas = np.zeros((300, 300, 3), dtype = "uint8")

#define color
#draw the line
#arguments are canvas/image, starting point, ending point, color, thickness(optional)
# disply in cv2 window
green = (0,255,0)
cv2.circle(canvas,(100,100), 10, green)
cv2.imshow("Single circle", canvas)
cv2.waitKey(0)

# draw concentric white circles
# calculate the centre point of canvas
# generate circles using for loop
# clearing the canvas
canvas = np.zeros((300, 300, 3), dtype = "uint8")
white = (255,255,255)
(centreX, centreY) = (canvas.shape[1]//2, canvas.shape[0]//2)

for r in range(0, 175, 25):
    cv2.circle(canvas,(centreX, centreY), r, white)

cv2.imshow("concentric circles", canvas)
cv2.waitKey(0)

