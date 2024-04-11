import cv2
import mediapipe as mp

# Init opencv & mediapipe
webcam = cv2.VideoCapture(0)
face_recognition = mp.solutions.face_detection.FaceDetection()
draw = mp.solutions.drawing_utils

while True:
    # Read webcam infos
    checker, image = webcam.read() # 2 answers, checker(bool) and image
    if not checker:
        break
    
    # Recognition faces
    list_face = face_recognition.process(image)
    
    if list_face.detections:
        for detection  in list_face.detections:
            draw.draw_detection(image, detection)
        cv2.imshow('Faces:', image)
    
    # When press ESC, quit app
    if cv2.waitKey(5) == 27:
        break
    
webcam.release()