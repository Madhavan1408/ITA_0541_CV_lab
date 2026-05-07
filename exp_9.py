import cv2

img = cv2.imread(r"D:\computer_vision\ferrari.jpeg")

rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Original", img)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()