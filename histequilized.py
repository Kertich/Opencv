import argparse
import numpy as np
from cv2 import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

#loading and converting the image into numpy array
image = cv2.imread(args["image"])

# BGR TO GRAY
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(gray)
cv2.imshow("Normal and Equilized",np.hstack([gray, eq]))
cv2.waitKey(0)