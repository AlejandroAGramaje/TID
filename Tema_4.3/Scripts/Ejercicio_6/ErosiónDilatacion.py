import cv2
import numpy as np

# Cargamos la imagen en escala de grises
img = cv2.imread('Tema_4.3/Sources/Perro.png', cv2.IMREAD_GRAYSCALE)

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Definimos un kernel cuadrado de 5x5
kernel = np.ones((5, 5), np.uint8)

# Aplicamos erosión (quita bordes blancos)
erosionada = cv2.erode(img_reducida, kernel, iterations=1)

# Aplicamos dilatación (agranda zonas blancas)
dilatada = cv2.dilate(img_reducida, kernel, iterations=1)

# Mostramos los resultados
cv2.imshow('Original reducida', img_reducida)
cv2.imshow('Erosionada', erosionada)
cv2.imshow('Dilatada', dilatada)
cv2.waitKey(0)
cv2.destroyAllWindows()
