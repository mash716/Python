import cv2

filename = "test.jpg"
gry = cv2.imread(filename, 0)
cv2.imwrite('gray.jpg', gry)