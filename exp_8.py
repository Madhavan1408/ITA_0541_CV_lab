import cv2

img = cv2.imread(r"D:\computer_vision\ferrari.jpeg")

# Check if image loaded properly
if img is None:
    print("Error: Image not loaded. Check file path!")
else:
    small = cv2.resize(img, (300, 300))
    cv2.imshow("Resized", small)
    cv2.waitKey(0)
    cv2.destroyAllWindows()