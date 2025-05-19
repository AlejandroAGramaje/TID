import numpy as np
import cv2 as cv

cap = cv.VideoCapture('Tema 4.4/Ejercicio_2/Video/videoKiddKeo.mp4')
imga = cv.cvtColor(cv.imread("Tema 4.4/Ejercicio_2/img/SoldadoImperio.jpg"), cv.COLOR_BGR2HSV)
Imga=cv.resize(imga,(300,300))
img2=Imga[0:500:2,0:1600:2,:]

while(cap.isOpened()):
    ret, frame = cap.read()
    rows,cols,channels = img2.shape
    roi = frame[0:rows, 0:cols]
    lowerBlue = np.array([85,40,50])
    upperBlue = np.array([135,255,255])
    mask = cv.inRange(img2, lowerBlue, upperBlue)
    mask_inv = cv.bitwise_not(mask)
    frame_bg = cv.bitwise_and(roi,roi,mask = mask)
    img2_fg = cv.cvtColor(cv.bitwise_and(img2,img2,mask = mask_inv),cv.COLOR_HSV2BGR)
    dst = cv.add(frame_bg,img2_fg)
    frame[0:rows, 0:cols ] = dst
    cv.imshow("img",frame)
    if cv.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()