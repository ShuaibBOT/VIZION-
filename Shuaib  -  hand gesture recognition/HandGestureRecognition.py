import cv2 as cv
import pickle
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp

#load model
with open('pickle_model', 'rb') as f:
    model = pickle.load(f)


cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

width, height = cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT ) #gets height and width of video frame
#print(width, height)
#WebWidth, WebHeight = 800,480
#cap.set(3,WebWidth)
#cap.set(4,WebHeight)
detector = HandDetector(detectionCon=0.8,maxHands=2)

#Starts Camera
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if not success:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #hands - dict {lmList,bbox,center,type}
    #hands consist of a landmark list, bounding box positions, center position,
    #and type of one hand.
    if hands:
        #Hands1
        hand1 = hands[0]
        lmList1 = hand1["lmList"] #List of 21 Landmark points.
        bbox1 = hand1["bbox"]#Bounding box info, consist of (x,y,w,h)
        centerPoint1 = hand1["center"] # center of the hand (cx,cy)
        handType1 = hand1["type"] #will give us the hand type (Left or Right)
        #print(bbox1) #prints bounding box
        #print(cv.circle(img,centerPoint1,20,(255,0,0),2))
        print(centerPoint1)
        #print(handType1)
        fingers1 = detector.fingersUp(hand1)
        #print(fingers1)
        if (len(hands)==2):
            # Hands1
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points.
            bbox2 = hand2["bbox"]  # Bounding box info, consist of (x,y,w,h)
            centerPoint2 = hand2["center"]  # center of the hand (cx,cy)
            handType2 = hand2["type"]  # will give us the hand type (Left or Right)
            fingers2 = detector.fingersUp(hand2)
            # print(fingers1,fingers2)
            #print(handType2)
            #print(fingers1, fingers2)
            cv.circle(img,centerPoint1,20,(255,0,0),2),cv.circle(img,centerPoint2,20,(255,0,0),2)
            if (handType2 == "Right" and handType1 == "Left"):



            elif (handType2 == "Left" and handType1 == "Right"):



        if (handType1 == "Right"):





        elif (handType1 == "Left"):





    cv.imshow("Image",img)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
