import cv2
import numpy as np

# Cargamos la imagen en color
img = cv2.imread("Tema_4.2/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Dividimos la imagen en canales B, G y R
b, g, r = cv2.split(img_reducida)

# Calculamos el histograma de cada canal
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Creamos una imagen negra para dibujar los histogramas
hist_img = np.zeros((512, 512, 3), np.uint8)
hist_max = max(np.max(hist_b), np.max(hist_g), np.max(hist_r))

# Dibujamos los histogramas de cada canal
for i in range(256):
    h_b = int(hist_b[i] * 512 / hist_max)
    h_g = int(hist_g[i] * 512 / hist_max)
    h_r = int(hist_r[i] * 512 / hist_max)
    cv2.line(hist_img, (i * 2, 512), (i * 2, 512 - h_b), (255, 0, 0))  # Azul
    cv2.line(hist_img, (i * 2, 512), (i * 2, 512 - h_g), (0, 255, 0))  # Verde
    cv2.line(hist_img, (i * 2, 512), (i * 2, 512 - h_r), (0, 0, 255))  # Rojo

# Mostramos el histograma combinado
cv2.imshow('Histograma de color (RGB)', hist_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardamos los histogramas en CSV
hist_combined = np.hstack([hist_b, hist_g, hist_r])
np.savetxt('histograma_color.csv', hist_combined, delimiter=',')
