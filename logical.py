import numpy as np 
from cv2 import cv2


#Create 300*300 numpy array and 250*250 white rectangle inside it
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("rectangle", rectangle)


#Create 300*300 numpy array and 150 radius white circle inside it
circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("circle", circle)

# performing the bitwise oprations
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr) 
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(rectangle, circle)
cv2.imshow("Not", bitwiseNot)
cv2.waitKey(0)
