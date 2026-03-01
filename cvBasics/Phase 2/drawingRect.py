import cv2

image = cv2.imread('python_image.png')

if image is None:
    print('Could not open or find the image.')
else:
    print("Image loaded successfully. Image shape:", image.shape)
    top_left = (50, 50)
    bottom_right = (300, 200)
    color = (255, 0, 0)  # Blue color in BGR
    thickness = 5
    cv2.rectangle(image, top_left, bottom_right, color, thickness)
    cv2.imshow('Rectangle Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()