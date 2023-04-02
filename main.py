import cv2
from cvzone.HandTrackingModule import HandDetector
from sys import argv


MINDIST = 35
SPECIAL_POINTS = {}

def MakeStable():
    x1, y1 = SPECIAL_POINTS["START"]
    x2, y2 = SPECIAL_POINTS["END"]
    
    x_min = min(x1, x2)
    x_max = max(x1, x2)

    y_min = min(y1, y2)
    y_max = max(y1, y2)

    FlipedFrame[y_min:y_max, x_min:x_max] = cv2.resize(OriginalIMG, (abs(x2 - x1), abs(y2 - y1)))

fname = argv[1]
OriginalIMG = cv2.imread(fname)
ROI = OriginalIMG.copy()

cap = cv2.VideoCapture(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

Detector = HandDetector(maxHands = 2, detectionCon = 0.8)

while True:
    re, frame = cap.read()

    FlipedFrame = cv2.flip(frame, 1)

    Hands, DrawedFrame = Detector.findHands(FlipedFrame, draw = True, flipType = False)

    if Hands:
        Left = Hands[0]
        Left_LmList = Left['lmList']
        
        True_Left_Distance = int(Detector.findDistance(Left_LmList[4][:2], Left_LmList[8][:2])[0])

        try:
            Right = Hands[1]
            Right_LmList = Right['lmList']
            
            True_Right_Distance = int(Detector.findDistance(Right_LmList[4][:2], Right_LmList[8][:2])[0])

            if True_Left_Distance <= MINDIST and True_Right_Distance <= MINDIST:
                Left_Host = Left['center']
                Right_Host = Right['center']
   

                SPECIAL_POINTS.update({"START": Left_Host})
                SPECIAL_POINTS.update({"END": Right_Host})
                
                cv2.rectangle(FlipedFrame, Left_Host, Right_Host, (0, 255, 255), 5)
                
                x1, y1 = Left_Host
                x2, y2 = Right_Host
                
                x_min = min(x1, x2)
                x_max = max(x1, x2)

                y_min = min(y1, y2)
                y_max = max(y1, y2)
                
                FlipedFrame[y_min:y_max, x_min:x_max] = cv2.resize(OriginalIMG, (abs(x2 - x1), abs(y2 - y1)))
        
        except:
            pass
        
    if len(SPECIAL_POINTS) == 2:
        MakeStable()

    cv2.imshow("Virtual Zoom", DrawedFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()