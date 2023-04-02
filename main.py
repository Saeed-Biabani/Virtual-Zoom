import cv2
from cvzone.HandTrackingModule import HandDetector
from sys import argv

cap = cv2.VideoCapture(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

Detector = HandDetector(maxHands = 2, detectionCon = 0.8)

while True:
    re, frame = cap.read()

    FlipedFrame = cv2.flip(frame, 1)

    Hands, DrawedFrame = Detector.findHands(FlipedFrame, draw = True, flipType = False)

    cv2.imshow("Virtual Zoom", DrawedFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()