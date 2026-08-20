import cv2
import requests

# Replace this with YOUR laptop's local IP address when testing on the same Wi-Fi
# (e.g., "http://192.168.1.15:8000/check_in/")
BACKEND_URL = "http://127.0.0.1:8000/check_in/"

# Initialize the webcam (0 is the default camera)
video_capture = cv2.VideoCapture(0)

print("Webcam started. Press 'q' to quit.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Display the live webcam feed on your friend's laptop screen
    cv2.imshow('AttendAI - Face Recognition Scanner', frame)

    # For testing right now: Press 's' to simulate detecting "Rudra Saha" and sending to backend
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        student_name = "Rudra Saha"
        try:
            response = requests.post(f"{BACKEND_URL}?name={student_name}&status=Present")
            print(f"Server Response: {response.json()}")
        except Exception as e:
            print(f"Connection Error: {e}")

    # Press 'q' to exit the webcam window
    if key == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()