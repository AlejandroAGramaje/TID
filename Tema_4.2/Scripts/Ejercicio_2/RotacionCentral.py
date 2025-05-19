import cv2

# Cargamos la imagen
img = cv2.imread("Tema_4.2/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Obtenemos las dimensiones de la imagen reducida
alto_r, ancho_r = img_reducida.shape[:2]

# Definimos el centro de la parte superior
centro = (ancho_r // 2, 0)

# Definimos la matriz de rotación (90° antihorario desde el centro superior)
M = cv2.getRotationMatrix2D(centro, 90, 1)

# Aplicamos la rotación
img_rotada = cv2.warpAffine(img_reducida, M, (ancho_r, alto_r))

# Guardamos la imagen rotada
cv2.imwrite("imagen_rotada.jpg", img_rotada)

# Mostramos las imágenes
cv2.imshow("Imagen reducida original", img_reducida)
cv2.imshow("Imagen rotada 90 grados", img_rotada)

# Esperamos a que el usuario presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
