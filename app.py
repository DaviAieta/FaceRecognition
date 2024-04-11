import cv2
import mediapipe as mp

# Init opencv & mediapipe
webcam = cv2.VideoCapture(0)
face_recognition = mp.solutions.face_detection.FaceDetection()
draw = mp.solutions.drawing_utils
