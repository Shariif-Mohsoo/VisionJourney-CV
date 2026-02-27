import cv2

image = cv2.imread('python_image.png')

if image is not None:
    cv2.imshow("Image Title", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not load the image.")
    