import cv2
import numpy as np

# Cargamos la imagen
img = cv2.imread("Tema_4.2/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Nuevas dimensiones
alto_r, ancho_r = img_reducida.shape[:2]

# Definimos tres puntos de origen y tres puntos de destino
src_pts = np.float32([[0, 0], [ancho_r - 1, 0], [0, alto_r - 1]])
dst_pts = np.float32([[50, 50], [ancho_r - 100, 100], [100, alto_r - 50]])

# Obtenemos la matriz de transformación afín
M = cv2.getAffineTransform(src_pts, dst_pts)

# Aplicamos la transformación afín
img_afín = cv2.warpAffine(img_reducida, M, (ancho_r, alto_r))

# Guardamos la imagen transformada
cv2.imwrite("imagen_transformada.jpg", img_afín)

# Mostramos las imágenes
cv2.imshow("Imagen original reducida", img_reducida)
cv2.imshow("Imagen transformada (afín)", img_afín)

# Esperamos a que el usuario presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
