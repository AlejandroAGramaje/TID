import cv2

img = cv2.imread('Tema 4.4/Ejercicio_1/img/matricula2.jpg')
imgGris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res = cv2.resize(imgGris, dsize=(54, 140), interpolation=cv2.INTER_CUBIC)

(thresh, im_bw) = cv2.threshold(imgGris, 128, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
thresh = 180 
im_bw1 = cv2.threshold(imgGris, thresh, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("imagenOriginal",img)
cv2.imshow("imagenGris", imgGris)
# cv2.imwrite('imagenAutomatica.jpg', im_bw)
cv2.imshow("imagenAutomatica", im_bw)
cv2.imshow("ImagenThresh", im_bw1)

cv2.waitKey(0)
cv2.destroyAllWindows() 