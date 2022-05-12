import cv2
import numpy

image = cv2.imread("Linus.jpg")
b, g, r = cv2.split(image)
zeros = numpy.zeros(b.shape, numpy.uint8)
b = cv2.merge((b, zeros, zeros))
g = cv2.merge((zeros, g, zeros))
r = cv2.merge((zeros, zeros, r))
cv2.imshow("Linus", image)
cv2.waitKey(0)
cv2.imshow("Blue Linus", b)
cv2.imshow("Green Linus", g)
cv2.imshow("Red Linus", r)
cv2.waitKey(0)
cv2.merge((cv2.cvtColor(b, cv2.COLOR_BGR2GRAY), zeros, zeros))
cv2.imshow("Modified Linus", cv2.cvtColor(b, cv2.COLOR_BGR2GRAY))
cv2.waitKey(0)
