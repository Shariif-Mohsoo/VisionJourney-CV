import cv2

img = cv2.imread('nature.jpg')
img = cv2.resize(img, (400, 400))

median_blur = cv2.medianBlur(img, 9)
median_blur = cv2.resize(median_blur, (600, 600))

cv2.imshow('Original Image', img)   
cv2.imshow('Median Blurred Image', median_blur) 

cv2.waitKey(0)  
cv2.destroyAllWindows()