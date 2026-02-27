import cv2

# user input
image_path = input("Enter the path to the image: ")

if image_path is not None:
    # read the image
    image = cv2.imread(image_path)
    # check if the image was loaded successfully
    if image is not None:
        # display the image
        cv2.imshow("Colored Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # conver the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # save the image
        save_name = input("Enter the name to save the grayscale image: ")
        if save_name is not None:
            cv2.imwrite(save_name, gray_image)
            print(f"Grayscale image saved as {save_name}")
        else:
            print("No save name provided. Grayscale image not saved.")
    else:
        print("Error: Could not load the image. Please check the path and try again.")
else:
    print("No image path provided. Exiting.")