import cv2

image = cv2.imread('python_image.png')

if image is None:
    print("Could not read the image.")
else:
    success = cv2.imwrite('saved_image.png', image)
    if success:
        print("Image saved successfully as 'saved_image.png'.")
    else:
        print("Failed to save the image.")
