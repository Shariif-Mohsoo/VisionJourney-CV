import cv2

image = cv2.imread('python_image.png')

if image is not None:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('grayscale_image.png', gray_image)
    print("Grayscale image saved as 'grayscale_image.png'.")
else:
    print("Error: Image not found.")