import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import socket
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras.models import load_model


#communication
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)

model = tf.keras.models.load_model('my_model')
# print(model.signatures)
#model = tf.saved_model.load('C:\\Users\\Thusal Athauda\\Documents\\GitHub\VIZION\\Deep learning model NEW\\my_model\\')

model.summary()
classNames = ["Blank","Rotation","Scale","Translation","X Rotation","X Scale","X Translation","Y Rotation","Y Scale","Y Translation","Z Rotation","Z Scale","Z Translation"]

cap = cv.VideoCapture(0)

width, height = cap.get(cv.CAP_PROP_FRAME_WIDTH ) ,cap.get(cv.CAP_PROP_FRAME_HEIGHT ) #gets height and width of video frame

detector = HandDetector(detectionCon=0.8,maxHands=2)

#Starts Camera
while True:
    success, img =cap.read()
    hands, img = detector.findHands(img)

    #image preparation
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = cv.resize(img, (224, 224))
    cv.imshow("prepared img", img)
    cv.waitKey(1)
    img = img.reshape(1, 224, 224, 3)

    centerPoints = []
    data = []
    #hands - dict {lmList,bbox,center,type}
    #hands consist of a landmark list, bounding box positions, center position,
    #and type of one hand.
    if hands:

        if (len(hands)==1):
            #Hands1
            hand1= hands[0]
            lmList1=hand1["lmList"]# List of 21 Landmark points.
            bbox1= hand1["bbox"]# Bounding box info, consist of (x,y,w,h)
            centerPoint1= hand1["center"] # center of the hand (cx,cy)
            handType1 = hand1["type"] #will give us the hand type (Left or Right)
            fingers1 = detector.fingersUp(hand1)
            #print(fingers1)

            if (handType1 == "Right"):

                prediction = model.predict(img)
                print(prediction)
                for i in range(13):
                    if prediction[0, i] == 1.0:
                        handClass = classNames[i]
                        print(classNames[i])

                data = fingers1[0], fingers1[1], fingers1[2], fingers1[3], \
                       fingers1[4], handClass
                centerPoints = data
                sock.sendto(str.encode(str(centerPoints)), serverAddressPort)


        if (len(hands)==2):
            # Hands2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points.
            bbox2 = hand2["bbox"]  # Bounding box info, consist of (x,y,w,h)
            centerPoint2 = hand2["center"]  # center of the hand (cx,cy)
            handType2 = hand2["type"]  # will give us the hand type (Left or Right)
            fingers2 = detector.fingersUp(hand2)

            prediction = model.predict(img)
            print(prediction)
            for i in range(13):
                if prediction[0, i] == 1.0:
                    handClass = classNames[i]
                    print(classNames[i])

            data = fingers1[0],fingers1[1],fingers1[2],fingers1[3],fingers1[4],fingers2[0],fingers2[1],fingers2[2],fingers2[3],fingers2[4],handClass
            centerPoints = data
            sock.sendto(str.encode(str(centerPoints)), serverAddressPort)
    else:
        handClass = 'Blank'
        data = "0","0","0","0","0","0",handClass
        centerPoints = data
        sock.sendto(str.encode(str(centerPoints)), serverAddressPort)
    # cv.imshow("Image",img)
    # cv.waitKey(1)