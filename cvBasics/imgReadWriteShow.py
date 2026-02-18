import cv2

img = cv2.imread(r"E:\computerVision\Assignment_0_232202022\screenshots\matplotlib.png")

# now this image is bascilly a red,green,blue scale img
print(img)

img = cv2.resize(img,(450,250))
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()