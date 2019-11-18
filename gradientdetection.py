import numpy as np
import argparse
from cv2 import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

#loading and converting the image into numpy array
image = cv2.imread(args["image"])

# convert image to greyscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# lapace gradient detection
lap = cv2.Laplacian(image, cv2.CV_64F)

# convert back to 8 bit usigned
lap = np.uint8(np.absolute(lap))

cv2.imshow("Laplace Gradient Detection", lap)


# Sobel X and Y
SobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
SobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

#convert back to 8 bit unsigned int
SobelX = np.uint8(np.absolute(SobelX))
SobelY = np.uint8(np.absolute(SobelY))

SobelCombined = cv2.bitwise_or(SobelX, SobelY)

cv2.imshow("Sobel X", SobelX)
cv2.imshow("Sobel Y", SobelY)
cv2.imshow("SobelCombined", SobelCombined)

cv2.waitKey(0)