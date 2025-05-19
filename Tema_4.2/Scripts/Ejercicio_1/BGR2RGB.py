import cv2

# Cargamos la imagen en formato BGR
img = cv2.imread("Tema_4.2/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Convertimos la imagen a formato RGB
img_rgb = cv2.cvtColor(img_reducida, cv2.COLOR_BGR2RGB)

# Guardamos la imagen en formato RGB en un archivo nuevo
cv2.imwrite("imagen_rgb.jpg", img_rgb)

# Mostramos la imagen original reducida y la imagen en formato RGB
cv2.imshow("Imagen original reducida", img_reducida)
cv2.imshow("Imagen en formato RGB", img_rgb)

# Esperamos a que el usuario presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
