import cv2

# Cargamos la imagen
img = cv2.imread("Tema_4.2/Sources/Perro.png")

# Obtenemos las dimensiones de la imagen
alto, ancho = img.shape[:2]

# Redimensionamos la imagen al 75%
img_redimensionada = cv2.resize(img, (int(ancho * 0.75), int(alto * 0.75)))

# Guardamos la imagen redimensionada en un archivo nuevo
cv2.imwrite("imagen_redimensionada.jpg", img_redimensionada)

# Mostramos la imagen original y la redimensionada
cv2.imshow("Imagen original", img)
cv2.imshow("Imagen redimensionada", img_redimensionada)

# Esperamos a que el usuario presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
