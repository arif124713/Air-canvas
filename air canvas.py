import cv2
import os
import numpy as np
import mediapipe as mp


import HandTrackingModule as htm

brushthickness=15
eraser=55
folder_path= "folder"
mylist = os.listdir(folder_path)
#print(mylist)
overlaylist= []
drawcolor= (255,0,255)

xp,yp= 0,0

imagecanvas= np.zeros((720,1280,3), np.uint8)


for impath in mylist:
    image= cv2.imread(f"{folder_path}/{impath}")
    overlaylist.append(image)

header= overlaylist[0]

cap= cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector= htm.handDetector(0.85)

while True:
    ret, frame = cap.read()
    #frame= cv2.flip(frame,1)
    frame= detector.findHands(frame)
    lmlist= detector.findPosition(frame,draw=False)

    if len(lmlist) > 0 and len(lmlist[0]) > 12:
        x1, y1 = lmlist[0][8][1], lmlist[0][8][2]
        x2, y2 = lmlist[0][12][1], lmlist[0][12][2]
        fingers = detector.fingersUp()


        if fingers[1] and fingers[2]:
            xp, yp = 0, 0
            print('selection mode')
            if y1<125:
                if 250<x1<450:
                    header = overlaylist[0]
                    drawcolor=(255,0,255)
                elif 550<x1<750:
                    header = overlaylist[1]
                    drawcolor = (0, 255, 0)
                elif 800<x1<950:
                    header = overlaylist[2]
                    drawcolor = (0, 0, 255)
                if 1050<x1<1200:
                    header = overlaylist[3]
                    drawcolor = (0, 0, 0)
            cv2.rectangle(frame, (x1, y1 - 25), (x2, y2 + 25), drawcolor, cv2.FILLED)


        if fingers[1] == 1 and fingers[2] == 0:
            cv2.circle(frame,(x1,y1),15,drawcolor,cv2.FILLED)
            print('drawing mode')

            if xp==0 and yp==0:
                xp,yp= x1,y1
            if drawcolor==(0,0,0):
                cv2.line(frame, (xp, yp), (x1, y1), color=drawcolor, thickness=eraser)
                cv2.line(imagecanvas, (xp, yp), (x1, y1), color=drawcolor, thickness=eraser)
                xp, yp = x1, y1

            else:
                cv2.line(frame,(xp,yp),(x1,y1),color=drawcolor,thickness=brushthickness)
                cv2.line(imagecanvas, (xp, yp), (x1, y1), color=drawcolor, thickness=brushthickness)
                xp,yp= x1,y1



    imgGray = cv2.cvtColor(imagecanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame,imgInv)
    frame = cv2.bitwise_or(frame,imagecanvas)


    frame[0:125,0:1280]= header
    #frame= cv2.addWeighted(frame,0.7,imagecanvas,0.3,0)
    cv2.imshow('frame', frame)
    cv2.imshow('canvas', imagecanvas)
    cv2.waitKey(1)