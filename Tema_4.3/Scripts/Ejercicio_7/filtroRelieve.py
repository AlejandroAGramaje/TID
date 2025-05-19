import cv2
import numpy as np

# Cargamos la imagen en escala de grises
img = cv2.imread('Tema_4.3/Sources/Perro.png', cv2.IMREAD_GRAYSCALE)

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Kernel para efecto relieve
kernel_relieve = np.array([[-2, -1, 0],
                           [-1,  1, 1],
                           [ 0,  1, 2]])

# Aplicamos el filtro de relieve
relieve = cv2.filter2D(img_reducida, -1, kernel_relieve)

# Ajustamos contraste sumando 128 (opcional)
relieve = cv2.convertScaleAbs(relieve + 128)

# Mostramos los resultados
cv2.imshow('Original reducida', img_reducida)
cv2.imshow('Relieve', relieve)
cv2.waitKey(0)
cv2.destroyAllWindows()
