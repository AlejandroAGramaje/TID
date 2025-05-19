import cv2
import numpy as np

# Cargamos la imagen en color
img = cv2.imread("Tema_4.3/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Creamos un kernel para simular el desenfoque de movimiento horizontal
size = 15
kernel_motion_blur = np.zeros((size, size))
kernel_motion_blur[int((size - 1) / 2), :] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size

# Aplicamos el kernel a la imagen
output = cv2.filter2D(img_reducida, -1, kernel_motion_blur)

# Mostramos las imágenes
cv2.imshow('Original reducida', img_reducida)
cv2.imshow('Motion Blur', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
