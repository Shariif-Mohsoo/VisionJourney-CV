import cv2

image = cv2.imread("python_image.png")

if image is not None:
    cropped_image = image[100:200, 50:150]
    print("Shape:", cropped_image.shape)
    cv2.imshow("Cropped Image", cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found.")