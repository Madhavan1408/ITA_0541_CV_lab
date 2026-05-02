import cv2

# Read image
image = cv2.imread(r'D:\computer_vision\ferrari.jpeg')

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Show results
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()