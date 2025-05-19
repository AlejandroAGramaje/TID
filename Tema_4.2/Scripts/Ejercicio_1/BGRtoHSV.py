import cv2

# Cargamos la imagen en formato BGR
img = cv2.imread("Tema_4.2/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Convertimos la imagen a formato HSV
img_hsv = cv2.cvtColor(img_reducida, cv2.COLOR_BGR2HSV)

# Guardamos la imagen en formato HSV en un archivo nuevo
cv2.imwrite("imagen_hsv.jpg", img_hsv)

# Mostramos la imagen original reducida y la imagen en formato HSV
cv2.imshow("Imagen original reducida", img_reducida)
cv2.imshow("Imagen en formato HSV", img_hsv)

# Esperamos a que el usuario presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
