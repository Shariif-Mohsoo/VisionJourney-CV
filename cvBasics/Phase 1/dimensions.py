import cv2

image = cv2.imread('python_image.png')

if image is None:
    print("Could not read the image.")
else:
    print("Image loaded successfully.")
    print("Image Dimensions:", image.shape)
    h,w,c = image.shape
    print("Height:", h)
    print("Width:", w)  
    print("Channels:", c)