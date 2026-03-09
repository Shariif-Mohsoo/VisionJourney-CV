import cv2

img = cv2.imread('flower.jfif', cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 50, 150)

cv2.imshow('Original Image', img)
cv2.imshow('Canny Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()