import cv2
import numpy as np

image = cv2.imread('img.jfif')
kernel = np.array([
                    [0, -1, 0],
                    [-1, 5, -1], 
                    [0, -1, 0]])
sharpened = cv2.filter2D(image, -1, kernel)
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()