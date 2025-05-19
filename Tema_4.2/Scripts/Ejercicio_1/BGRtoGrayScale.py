import cv2

# Cargamos la imagen en formato BGR
img = cv2.imread("Tema_4.2/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Convertimos la imagen a escala de grises
img_gris = cv2.cvtColor(img_reducida, cv2.COLOR_BGR2GRAY)

# Guardamos la imagen en escala de grises en un archivo nuevo
cv2.imwrite("imagen_gris.jpg", img_gris)

# Mostramos la imagen redimensionada original y la imagen en escala de grises
cv2.imshow("Imagen original reducida", img_reducida)
cv2.imshow("Imagen en escala de grises", img_gris)

# Esperamos a que el usuario presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()