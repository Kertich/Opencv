import argparse
from cv2 import cv2

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Enter path to the image")
args = vars(ap.parse_args())

#loading and converting the image into numpy array
#prining the corresponding values
image = cv2.imread(args["image"])
print("width of the image in pixels is {}: ".format(image.shape[1]))
print("height of the image in pixels is {}: ".format(image.shape[0]))
print("channels present the image in pixels is {}: ".format(image.shape[2]))

# load image into cv2 window
# wait for key press
# write image into another format
cv2.imshow("Image Title", image)
cv2.waitKey(5000)
cv2.imwrite("newcat.jpg", image)