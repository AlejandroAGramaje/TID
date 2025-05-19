import cv2
import numpy as np

# Cargamos la imagen
img = cv2.imread("Tema_4.2/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Nuevas dimensiones
alto_r, ancho_r = img_reducida.shape[:2]

# Definimos la matriz de transformación para la traslación
M = np.float32([[1, 0, 100], [0, 1, 50]])

# Aplicamos la traslación a la imagen
img_trasladada = cv2.warpAffine(img_reducida, M, (ancho_r, alto_r))

# Guardamos la imagen trasladada en un archivo nuevo
cv2.imwrite("imagen_trasladada.jpg", img_trasladada)

# Mostramos la imagen reducida original y la trasladada
cv2.imshow("Imagen reducida original", img_reducida)
cv2.imshow("Imagen trasladada", img_trasladada)

# Esperamos a que el usuario presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
