import cv2
import numpy as np

# Creamos una imagen blanca de fondo y la redimensionamos a la mitad
imagen = 255 * np.ones((400, 600, 3), dtype=np.uint8)
imagen_reducida = cv2.resize(imagen, (300, 200))

# Dibujamos dos rectángulos verdes
cv2.rectangle(imagen_reducida, (25, 40), (75, 90), (0, 255, 0), 3)   # Borde verde
cv2.rectangle(imagen_reducida, (125, 40), (175, 90), (0, 255, 0), -1) # Relleno verde

# Mostramos la imagen con los rectángulos
cv2.imshow('Imagen con rectángulos', imagen_reducida)
cv2.waitKey(0)
cv2.destroyAllWindows()
