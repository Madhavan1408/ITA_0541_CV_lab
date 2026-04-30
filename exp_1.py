import cv2

image = cv2.imread(r'D:\computer_vision\ferrari.jpeg')

if image is None:
    print("Error: Image not loaded")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Show images (no assignment)
    cv2.imshow("Original", image)
    cv2.imshow("Gray", gray_image)
    cv2.imwrite("gray_scale_image.jpg",gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()