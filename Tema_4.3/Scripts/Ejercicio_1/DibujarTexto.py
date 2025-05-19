import cv2
import numpy as np

# Creamos una imagen blanca de fondo y la redimensionamos a la mitad
imagen = 255 * np.ones((400, 600, 3), dtype=np.uint8)
imagen_reducida = cv2.resize(imagen, (300, 200))

# Fuente del texto
font = cv2.FONT_HERSHEY_SIMPLEX

# Dibujamos texto en la imagen
cv2.putText(imagen_reducida, 'OpenCV', (10, 50), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

# Mostramos la imagen con el texto
cv2.imshow('Imagen con texto', imagen_reducida)
cv2.waitKey(0)
cv2.destroyAllWindows()
