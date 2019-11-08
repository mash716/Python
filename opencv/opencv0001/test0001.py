import cv2
import os

filename = "test.jpg"
gryr = cv2.imread(filename, 0)

print(os.path.exists("test.jpg"))

#C://Users//masho//Desktop//gray.jpg
gryw = cv2.imwrite('C://aaa//gray.jpg', gryr)

print(os.path.exists("C://aaa//gray.jpg"))