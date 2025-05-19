import cv2
import numpy as np

# Cargamos la imagen en color
img = cv2.imread('Tema_4.3/Sources/Perro.png')

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))
alto_r, ancho_r = img_reducida.shape[:2]

# Creamos una máscara tipo viñeta con una distribución gaussiana
kernel_x = cv2.getGaussianKernel(ancho_r, 200)
kernel_y = cv2.getGaussianKernel(alto_r, 200)
kernel = kernel_y @ kernel_x.T
mascara = kernel / kernel.max()

# Aplicamos la máscara a cada canal (BGR)
viñeta = np.empty_like(img_reducida, dtype=np.uint8)
for i in range(3):
    viñeta[:, :, i] = img_reducida[:, :, i] * mascara

# Mostramos el resultado
cv2.imshow('Original reducida', img_reducida)
cv2.imshow('Filtro viñeta', viñeta)
cv2.waitKey(0)
cv2.destroyAllWindows()
