import cv2


image = cv2.imread('python_image.png')

if image is None:
    print('Could not open or find the image.')
else:
    print("Image loaded successfully. Image shape:", image.shape)
    pt1 = (50,100)
    pt2 =(300,100)
    color = (0,255,0)
    thickness = 5
    cv2.line(image, pt1, pt2, color, thickness)
    cv2.imshow('Line Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()