import cv2
import numpy as np

image = cv2.imread(r'D:\computer_vision\ferrari.jpeg', 0)
equalized = cv2.equalizeHist(image)

# Combine images horizontally
comparison = np.hstack((image, equalized))

cv2.imshow("Original vs Equalized", comparison)
cv2.waitKey(0)
cv2.destroyAllWindows()