import argparse
import imutils
from cv2 import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

#loading and converting the image into numpy array
#prining the corresponding values
image = cv2.imread(args["image"])

# rotate the image
rotated = imutils.rotate(image, 100)
cv2.imshow("180 rotated", rotated)
cv2.waitKey(0)


