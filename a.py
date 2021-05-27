import cv2
import numpy as np
import imutils
from random import randint

def Compare(Coorx,Coory):
    if(340<Coorx<360 and 43<Coory<63):
        Jenga[0]=1
    elif(210<Coorx<230 and 44<Coory<64):
        Jenga[1]=1
    elif(342<Coorx<362 and 122<Coory<142):
        Jenga[2]=1
    elif(213<Coorx<233 and 123<Coory<143):
        Jenga[3]=1
    elif(348<Coorx<368 and 204<Coory<244):
        Jenga[4]=1
    elif(213<Coorx<233 and 206<Coory<226):
        Jenga[5]=1
    elif(353<Coorx<373 and 285<Coory<305):
        Jenga[6]=1
    elif(218<Coorx<238 and 288<Coory<308):
        Jenga[7]=1
    #228 298
    #363 295
    #223 215
    #358 214
    #223 134
    #354 131
    #220 54
    #351 52
def my_custom_random():
  
  arr = np.array(Jenga)

  exclude=np.ndarray.flatten(np.where(arr == 0)[0])
  randInt = randint(0,7)
  
  return my_custom_random() if randInt in exclude else randInt

cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
Jenga=[0,0,0,0,0,0,0,0]

while True:
     _,frame= cap.read()
     exclude=[10,11,12,13,14,15,16,17]
     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

     lower_red = np.array([0,50,120])
     upper_red = np.array([10,255,255])

     mask = cv2.inRange(hsv,lower_red,upper_red)

     cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     cnts = imutils.grab_contours(cnts)
     jengacount = [8,8]
     loopNumb = 0
     
     for c in cnts:
         area = cv2.contourArea(c)
         if area > 2000:
            


             cv2.drawContours(frame,[c],-1,(0,255,0), 3)
             
             M = cv2.moments(c)
             
             cx = int(M["m10"]/ M["m00"])
             cy = int(M["m01"]/ M["m00"])
             
             Compare(cx,cy)     
             
             #flag++   
             #if flag>maxFlag:
                #flag=0 
            
             cv2.circle(frame,(cx,cy),7,(255,255,255),-1)
             
     cv2.imshow("result",frame)
     
    
     print("jengadata is ",Jenga)
     
     
     
     
     print("Jenga number to send",my_custom_random())
        
     Jenga=[0,0,0,0,0,0,0,0]   
     k = cv2.waitKey(5)
     if k == 27:
         break
 
cap.release()
cv2.destroyAllWindows()
import serial
arData = serial.Serial('COM4',9600)
arData.write('2')
arData.write('6')
