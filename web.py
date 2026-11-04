
import cv2

# Access webcam
cap = cv2.VideoCapture(0)

while True:

    # Read webcam frame
    success, frame = cap.read()

    if not success:
        print("Cannot access webcam")
        break

    # Mirror the frame
    frame = cv2.flip(frame, 1)

    # Display webcam
    cv2.imshow("Retro Lens - Webcam", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
cap.release()
cv2.destroyAllWindows()
