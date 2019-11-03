import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt
# read an image
img = cv2.imread('test.jpg')

# show image format (basically a 3-d array of pixel color info, in BGR format)
print(img)