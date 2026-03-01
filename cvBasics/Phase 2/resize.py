import cv2

image = cv2.imread('python_image.png')

if image is None:
    print("Could not read the image.")
else:
    # Resize the image to 300x300 pixels
    resized_image = cv2.resize(image, (300, 300))
    # Display the original and resized images
    cv2.imshow('Original Image', image)
    cv2.imshow('Resized Image', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 