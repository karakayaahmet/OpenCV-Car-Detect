import cv2

cap = cv2.VideoCapture("car.mp4")

car_cascade = cv2.CascadeClassifier("car.xml")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640,480))
    