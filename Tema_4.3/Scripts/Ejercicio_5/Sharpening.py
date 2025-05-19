import cv2
import numpy as np

# Cargamos la imagen en color
img = cv2.imread("Tema_4.3/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Definimos tres kernels distintos para realzar bordes
kernel_sharp_1 = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]])

kernel_sharp_2 = np.array([[ 1,  1,  1],
                           [ 1, -7,  1],
                           [ 1,  1,  1]])

kernel_sharp_3 = np.array([[-1, -1, -1, -1, -1],
                           [-1,  2,  2,  2, -1],
                           [-1,  2,  8,  2, -1],
                           [-1,  2,  2,  2, -1],
                           [-1, -1, -1, -1, -1]]) / 8.0

# Aplicamos los filtros
out1 = cv2.filter2D(img_reducida, -1, kernel_sharp_1)
out2 = cv2.filter2D(img_reducida, -1, kernel_sharp_2)
out3 = cv2.filter2D(img_reducida, -1, kernel_sharp_3)

# Mostramos las imágenes
cv2.imshow('Original reducida', img_reducida)
cv2.imshow('Sharpening básico', out1)
cv2.imshow('Sharpening fuerte', out2)
cv2.imshow('Realce de bordes suave', out3)
cv2.waitKey(0)
cv2.destroyAllWindows()
