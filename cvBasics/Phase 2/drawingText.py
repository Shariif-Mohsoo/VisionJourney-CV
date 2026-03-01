import cv2

image = cv2.imread('python_image.png')

if image is None:
    print('Could not open or find the image.')
else:
    print("Image loaded successfully. Image shape:", image.shape) 
    cv2.putText(image,"Hello World!",(500,350),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,255,0),2)
    cv2.imshow('Image with Text', image)
    cv2.waitKey(0)          
    cv2.destroyAllWindows()