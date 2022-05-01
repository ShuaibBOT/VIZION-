import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import socket

#communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)

cap = cv.VideoCapture(0)

width, height = cap.get(cv.CAP_PROP_FRAME_WIDTH ) ,cap.get(cv.CAP_PROP_FRAME_HEIGHT ) #gets height and width of video frame
#print(width, height)
#WebWidth, WebHeight = 800,480
#cap.set(3,WebWidth)
#cap.set(4,WebHeight)
detector = HandDetector(detectionCon=0.8,maxHands=2)

#Starts Camera
while True:
    success, img =cap.read()
    hands, img = detector.findHands(img)

    centerPoints = []
    data = []
    #hands - dict {lmList,bbox,center,type}
    #hands consist of a landmark list, bounding box positions, center position,
    #and type of one hand.
    if hands:
        #Hands1
        hand1= hands[0]
        lmList1=hand1["lmList"]# List of 21 Landmark points.
        bbox1= hand1["bbox"]# Bounding box info, consist of (x,y,w,h)
        centerPoint1= hand1["center"] # center of the hand (cx,cy)
        handType1 = hand1["type"] #will give us the hand type (Left or Right)
        #print(bbox1) #prints bounding box
        #print(cv.circle(img,centerPoint1,20,(255,0,0),2))
        #print(centerPoint1)
        #print(handType1)
        fingers1 = detector.fingersUp(hand1)
        #print(fingers1)
        if (handType1 == "Left"):
            if (fingers1[0] == 0 and fingers1[1] == 0 and fingers1[2] == 0 and fingers1[3] == 0 and fingers1[4] == 0):
                cv.putText(img, "Grab", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
            elif (fingers1[0] == 1 and fingers1[1] == 0 and fingers1[2] == 0 and fingers1[3] == 0 and fingers1[4] == 0):
                cv.putText(img, "Rotate", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
            elif (fingers1[0] == 1 and fingers1[1] == 1 and fingers1[2] == 0 and fingers1[3] == 0 and fingers1[4] == 0):
                cv.putText(img, "Scaling", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
            else:
                cv.putText(img, "Not Recognized", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

            data = centerPoint1[0], centerPoint1[1],fingers1[0],fingers1[1],fingers1[2],fingers1[3],fingers1[4],handType1
            centerPoints = data
            sock.sendto(str.encode(str(centerPoints)), serverAddressPort)

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
            #print(centerPoint2)
            cv.circle(img,centerPoint1,20,(255,0,0),2),cv.circle(img,centerPoint2,20,(255,0,0),2)

            data = centerPoint1[0], centerPoint1[1],centerPoint2[0], centerPoint2[1],fingers1[0],fingers1[1],fingers1[2],fingers1[3],fingers1[4],fingers2[0],fingers2[1],fingers2[2],fingers2[3],fingers2[4],handType1,handType2
            centerPoints = data
            sock.sendto(str.encode(str(centerPoints)), serverAddressPort)

            if (handType2 == "Right" and handType1 == "Left"):

                if (fingers2==[1,0,1,1,1] and fingers1 == [0,0,0,0,0]):  # Grab - Z axis
                    cv.putText(img, "Grab - Z axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 == [1,0,1,1,1] and fingers1 == [1,0,0,0,0]):  # Rotation - Z axis
                    cv.putText(img, "Rotation - Z axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 == [1,0,1,1,1] and fingers1 == [1,1,0,0,0]):  # Scaling - Z axis
                    cv.putText(img, "Scaling - Z axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 == [0,1,1,0,0] and fingers1 == [0,0,0,0,0]): # Grab - Y axis
                    cv.putText(img, "Grab - Y axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)


                elif (fingers2 == [0,1,1,0,0] and fingers1 == [1,0,0,0,0]):  # Rotation - Y axis
                    cv.putText(img, "Rotation - Y axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 == [0,1,1,0,0] and fingers1 == [1,1,0,0,0]):  # Scaling - Y axis
                    cv.putText(img, "Scaling - Y axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 == [1,0,0,0,1] and fingers1 == [0,0,0,0,0] ): # Grab - X axis
                    cv.putText(img, "Grab - X axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 == [1,0,0,0,1] and fingers1 == [1,0,0,0,0]):  # Rotation - X axis
                    cv.putText(img, "Rotation - X axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 == [1,0,0,0,1] and fingers1 == [1,1,0,0,0]):  # Scaling - X axis
                    cv.putText(img, "Scaling - X axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                else:
                    cv.putText(img, "Not Recognized", (200, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            elif (handType2 == "Left" and handType1 == "Right"):

                if(fingers2==[0,0,0,0,0] and fingers1 == [1,0,1,1,1]): # Grab - Z axis
                    cv.putText(img, "Grab - Z axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 ==[0,0,0,0,0] and fingers1 == [0,1,1,0,0]): #Grab - Y axis
                        cv.putText(img, "Grab - Y axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 ==[0,0,0,0,0] and fingers1 == [1,0,0,0,1]): #Grab - X axis
                        cv.putText(img, "Grab - X axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 ==[1,0,0,0,0] and fingers1 == [1,0,1,1,1]): #Rotation - Z axis
                    cv.putText(img, "Rotation - Z axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 ==[1,0,0,0,0] and fingers1 == [0,1,1,0,0]):  #Rotation - Y axis
                        cv.putText(img, "Rotation - Y axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 ==[1,0,0,0,0] and fingers1 == [1,0,0,0,1]):  #Rotation - X axis
                        cv.putText(img, "Rotation - X axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 ==[1,1,0,0,0] and fingers1 == [1,0,1,1,1]): #Scaling - Z axis
                    cv.putText(img, "Scaling - Z axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 ==[1,1,0,0,0] and fingers1 == [0,1,1,0,0]):  #Scaling - Y axis
                        cv.putText(img, "Scaling - Y axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                elif (fingers2 ==[1,1,0,0,0] and fingers1 == [1,0,0,0,1]):  #Scaling - X axis
                        cv.putText(img, "Scaling - X axis", (100, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
                else:
                    cv.putText(img, "Not Recognized", (300, 100), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # data = []
    #
    # for d in
        # if (handType1 == "Right"):
        #
        #
        #      if(fingers1[0]==1 and fingers1[1]==0 and fingers1[2]==1 and fingers1[3]==1 and fingers1[4]==1):
        #          cv.putText(img,"Z axis",(50,50),cv.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255), 2)
        #      elif(fingers1[0]==0 and fingers1[1]==1 and fingers1[1]==1 and fingers1[3]==0 and fingers1[4]==0):
        #          cv.putText(img, "Y axis", (50, 50),cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        #      elif(fingers1[0]==1 and fingers1[1]==0 and fingers1[1]==0 and fingers1[3]==0 and fingers1[4]==1):
        #          cv.putText(img, "X axis", (50, 50),cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        #      else:
        #          cv.putText(img, "Not Recognized", (50, 50),cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        #
        #
        # elif (handType1 == "Left"):
        #
        #
        #      if (fingers1[0] == 0 and fingers1[1] == 0 and fingers1[2] == 0 and fingers1[3] == 0 and fingers1[4] == 0):
        #          cv.putText(img, "Grab", (50, 50),cv.FONT_HERSHEY_SIMPLEX,1, (255, 0, 255), 2)
        #      elif (fingers1[0] == 1 and fingers1[1] == 0 and fingers1[2] == 0 and fingers1[3] == 0 and fingers1[4] == 0):
        #          cv.putText(img, "Rotate", (50, 50),cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
        #      elif (fingers1[0] == 1 and fingers1[1] == 1 and fingers1[2] == 0 and fingers1[3] == 0 and fingers1[4] == 0):
        #          cv.putText(img, "Scaling", (50, 50),cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
        #      else:
        #          cv.putText(img, "Not Recognized", (50, 50),cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)



    cv.imshow("Image",img)
    cv.waitKey(1)