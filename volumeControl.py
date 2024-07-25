import cv2
import mediapipe as mp
import pyautogui

# Initialize variables
x1 = y1 = x2 = y2 = 0

# Set up webcam capture
webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    # Read frame from webcam
    _, image = webcam.read()
    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)
    frame_height, frame_width, _ = image.shape
    # Convert the BGR image to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Process the RGB image to find hands
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:  # Index finger tip
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                    x1 = x
                    y1 = y
                if id == 4:  # Thumb tip
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                    x2 = x
                    y2 = y
        # Calculate the distance between thumb tip and index finger tip
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 // 4
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)
        # Control the volume based on the distance
        if dist > 50:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")

    # Display the resulting frame
    cv2.imshow("Hand volume control using Python", image)

    # Break the loop when 'ESC' is pressed
    key = cv2.waitKey(10)
    if key == 27:
        break

# Release the webcam and close windows
webcam.release()
cv2.destroyAllWindows()