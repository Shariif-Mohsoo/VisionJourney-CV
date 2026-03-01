import cv2

image = cv2.imread('python_image.png')

if image is None:
    print('Could not open or find the image.')
else:
    print("Image loaded successfully. Image shape:", image.shape)
    # Draw a circle on the image
    center_coordinates = (250, 250)  # Center of the circle (x, y)
    radius = 100  # Radius of the circle
    color = (0, 0, 255)  # Red color in BGR
    thickness = 5  # Thickness of the circle outline
    cv2.circle(image, center_coordinates, radius, color, thickness)
    cv2.imshow('Circle Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()