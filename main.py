import cv2
from cvzone.HandTrackingModule import HandDetector
from sys import argv

cap = cv2.VideoCapture(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    re, frame = cap.read()

    cv2.imshow("Virtual Zoom", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()