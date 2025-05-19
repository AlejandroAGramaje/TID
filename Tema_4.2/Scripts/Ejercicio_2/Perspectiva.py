import cv2
import numpy as np

# Cargamos la imagen
img = cv2.imread("Tema_4.2/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Nuevas dimensiones
alto_r, ancho_r = img_reducida.shape[:2]

# Definimos cuatro puntos de origen y destino para la transformación
src_pts = np.float32([[0, 0], [ancho_r - 1, 0], [0, alto_r - 1], [ancho_r - 1, alto_r - 1]])
dst_pts = np.float32([[50, 50], [ancho_r - 100, 100], [100, alto_r - 50], [ancho_r - 50, alto_r - 100]])

# Obtenemos la matriz de transformación en perspectiva
M = cv2.getPerspectiveTransform(src_pts, dst_pts)

# Aplicamos la transformación en perspectiva
img_perspectiva = cv2.warpPerspective(img_reducida, M, (ancho_r, alto_r))

# Guardamos la imagen transformada
cv2.imwrite("imagen_transformada.jpg", img_perspectiva)

# Mostramos las imágenes
cv2.imshow("Imagen original reducida", img_reducida)
cv2.imshow("Imagen transformada (perspectiva)", img_perspectiva)

# Esperamos a que el usuario presione una tecla para cerrar las ventanas
cv2.waitKey(0)
