import cv2
import numpy as np

# Creamos una imagen blanca de fondo y la redimensionamos a la mitad
imagen = 255 * np.ones((400, 600, 3), dtype=np.uint8)
imagen_reducida = cv2.resize(imagen, (300, 200))

# Dibujamos dos círculos
cv2.circle(imagen_reducida, (150, 100), 50, (255, 0, 0), -1)   # Círculo azul relleno
cv2.circle(imagen_reducida, (150, 100), 10, (0, 255, 255), 3)  # Círculo amarillo de borde

# Mostramos la imagen con los círculos
cv2.imshow('Imagen con círculos', imagen_reducida)
cv2.waitKey(0)
cv2.destroyAllWindows()
