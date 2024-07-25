# hand-gesture-volume-control

Overview
This project demonstrates how to control the system volume using hand gestures, implemented with Python and the OpenCV library.

Steps to Develop the Project
Install and Import Libraries: Begin by installing and importing the necessary libraries using PyCharm: OpenCV, pyautogui, and mediapipe.
Capture Webcam Video: Use OpenCV to access the webcam and display the video feed with the imshow function.
Hand Detection with MediaPipe: Utilize the mediapipe library to detect and track hand landmarks in the video feed.
Identify Thumb and Forefinger Landmarks: Pinpoint the landmarks for the thumb and forefinger, drawing lines between them.
Calculate Distance Between Points: Learn to calculate the distance between the two identified points.
Control Volume with PyAutoGUI: Adjust the system volume based on the distance between the thumb and forefinger using the pyautogui library.
Technologies Used
Python: The main programming language for the project.
OpenCV: For capturing and displaying video from the webcam.
MediaPipe: For detecting and tracking hand landmarks.
PyAutoGUI: For adjusting the system volume based on hand gestures.
Acknowledgements
OpenCV: For providing powerful computer vision functionalities.
MediaPipe: For its advanced hand tracking and landmark detection capabilities.
PyAutoGUI: For enabling seamless control of system functions.
Check it out here: Hand Gesture Volume Control 💻🎉
