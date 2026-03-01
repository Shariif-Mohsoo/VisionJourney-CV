import cv2


image = cv2.imread("python_image.png")

if image is None:
    print("Could not read the image.")
else:
    # Get the dimensions of the image 
    (height,width) = image.shape[:2]
    # Calculate the center of the image
    center = (width // 2, height // 2)
    M = cv2.getRotationMatrix2D(center,-90,1.0)
    rotated_image = cv2.warpAffine(image,M,(width,height))
    cv2.imshow("Original Image",image)
    cv2.imshow("Rotated Image",rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()