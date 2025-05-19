import cv2
import numpy as np

# Cargamos la imagen en color
img = cv2.imread("Tema_4.3/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Convertimos al espacio de color YUV
img_yuv = cv2.cvtColor(img_reducida, cv2.COLOR_BGR2YUV)

# Ecualizamos el canal de luminancia (Y)
img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])

# Convertimos de nuevo a BGR
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

# Mostramos las imágenes
cv2.imshow('Original reducida', img_reducida)
cv2.imshow('Ecualizada YUV', img_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
