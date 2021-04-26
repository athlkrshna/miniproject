import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)


# [66,188,0,86,255,255] vaishnav
# [90,48,0,118,255,255] athul

myColors = [[104,39,136,179,255,255]]
            #[[5,107,0,19,255,255]]
            #[133,56,0,159,156,255] 
            #[57,76,0,100,255,255],
            #[90,48,0,118,255,255]
            # [59,72,163,83,255,255]
myColorValues = [[0,0,0]]         ## BGR
                #[51,153,255]
                 #[255,0,255],
                 #[0,255,0],
                 #[255,0,0]]

myPoints =  []  ## [x , y , colorId ]

def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),15,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        #cv2.imshow(str(color[0]),mask)
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
            
    p1,p2=x+w//2,y
    # if p1<=140 and p1>=40 and p2<=65 and p2>=1:
    #     imgResult = np.zeros([480,640,3],dtype=np.uint8)
    #     imgResult.fill(255)
    #     frame = cv2.rectangle(imgResult, (40, 1), (140, 65), (122, 122, 122), -1)
    # print(p1,p2)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        print(point)
        cv2.circle(imgResult, (point[0], point[1]), 5, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img1 = cap.read()
    img= cv2.flip(img1, 1)
    if img is None:
        break
    imgResult = np.zeros([480,640,3],dtype=np.uint8)
    imgResult.fill(255)
    frame = cv2.rectangle(imgResult, (40, 1), (140, 65), (122, 122, 122), -1)
    cv2.putText(frame, "CLEAR ALL", (49, 33),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255, 255, 255), 2, cv2.LINE_AA)
    newPoints = findColor(img, myColors,myColorValues)
    flag=0
    if len(newPoints)!=0:
        for newP in newPoints:
            if 40<= newP[0]<= 140 and newP[1]<=65:
                flag=1
                #imgResult = np.zeros([480,640,3],dtype=np.uint8)
                #imgResult.fill(255)
            else:
                myPoints.append(newP)
    if len(myPoints)!=0:
        if flag==1:
            myPoints=[]

        drawOnCanvas(myPoints,myColorValues)
    
  

    cv2.imshow("Aircanvas", imgResult)
    