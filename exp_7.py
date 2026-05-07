import cv2

# Open video file (0 for webcam OR give file path)
cap = cv2.VideoCapture(0)   # change to "video.mp4" if using file

if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("End of video or error")
        break

    # Show normal video
    cv2.imshow("Normal Video", frame)

    # -------- Slow Motion --------
    # Show same frame multiple times (slower effect)
    cv2.imshow("Slow Motion", frame)
    cv2.waitKey(80)   # increase delay = slower video

    # -------- Fast Motion --------
    # Skip frames to make it faster
    for i in range(2):   # skip 2 frames
        cap.read()

    cv2.imshow("Fast Motion", frame)
    cv2.waitKey(10)   # small delay = faster video

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()