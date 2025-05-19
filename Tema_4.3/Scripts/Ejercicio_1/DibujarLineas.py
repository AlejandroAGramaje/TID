import cv2
import numpy as np

# Creamos una imagen en blanco redimensionada a la mitad (200x300)
imagen = 255 * np.ones((400, 600, 3), dtype=np.uint8)
imagen_reducida = cv2.resize(imagen, (300, 200))

# Dibujamos dos líneas
cv2.line(imagen_reducida, (0, 0), (300, 200), (255, 0, 0), 4)     # Línea azul
cv2.line(imagen_reducida, (150, 0), (150, 100), (0, 0, 255), 10)  # Línea roja

# Mostramos la imagen
cv2.imshow('Imagen con lineas', imagen_reducida)
cv2.waitKey(0)
cv2.destroyAllWindows()
