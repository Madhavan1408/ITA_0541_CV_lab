import cv2

# Read image in grayscale
image = cv2.imread(r'D:\computer_vision\ferrari.jpeg', 0)

# Apply Histogram Equalization
equalized = cv2.equalizeHist(image)

# Show results
cv2.imshow("Original Image", image)
cv2.imshow("Equalized Image", equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()