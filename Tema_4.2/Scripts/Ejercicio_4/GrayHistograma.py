import cv2
import numpy as np

# Cargamos la imagen en color
img = cv2.imread("Tema_4.2/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Convertimos a escala de grises
gray = cv2.cvtColor(img_reducida, cv2.COLOR_BGR2GRAY)

# Calculamos el histograma
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Creamos una imagen negra para dibujar el histograma
hist_img = np.zeros((512, 512, 3), np.uint8)
hist_max = np.max(hist)

# Dibujamos el histograma
for i in range(256):
    valor = int(hist[i] * 512 / hist_max)
    cv2.line(hist_img, (i * 2, 512), (i * 2, 512 - valor), (255, 255, 255))

# Mostramos el histograma
cv2.imshow('Histograma', hist_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardamos el histograma en un archivo CSV
np.savetxt('histograma_opencv.csv', hist, delimiter=',')
