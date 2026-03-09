"""
Bitwise Operations
print("Bitwise Operations")

cv2.bitwise_and(src1, src2)
cv2.bitwise_or(src1, src2)
cv2.bitwise_not(src1)


@ img1 and img2 are the input images, which should be of the same size and type.
@ use only black and white images (binary images) for better visualization of the results.
"""

import cv2
import numpy as np

# Create two black images
img1 = np.zeros((300, 300), dtype=np.uint8)
img2 = np.zeros((300, 300), dtype=np.uint8)

cv2.circle(img1, (150, 150), 100, 255, -1)  # Draw a white circle on img1
cv2.rectangle(img2, (100, 100), (250, 250), 255, -1)  # Draw a white rectangle on img2
# Perform bitwise operations
bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2) 
bitwise_not = cv2.bitwise_not(img1)
# Display the results
cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2) 
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise NOT", bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()