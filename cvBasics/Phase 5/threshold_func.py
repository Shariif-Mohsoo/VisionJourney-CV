import cv2

img = cv2.imread('flower.jfif', cv2.IMREAD_GRAYSCALE)

ret,thres_img = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thres_img)
cv2.waitKey(0)
cv2.destroyAllWindows()