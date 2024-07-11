import numpy as np
import cv2

cap = cv2.VideoCapture("rtsp://192.168.137.17:8554")

while True:
    ret, frame = cap.read()
    cv2.imshow('d', frame)
    cv2.waitKey(1)
