import cv2

# Cargamos la imagen en color
img = cv2.imread("Tema_4.3/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Convertimos la imagen a escala de grises
img_gris = cv2.cvtColor(img_reducida, cv2.COLOR_BGR2GRAY)

# Aplicamos los filtros Sobel en dirección horizontal y vertical
sobel_horizontal = cv2.Sobel(img_gris, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv2.Sobel(img_gris, cv2.CV_64F, 0, 1, ksize=5)

# Mostramos las imágenes
cv2.imshow('Original reducida', img_reducida)
cv2.imshow('Sobel Horizontal', sobel_horizontal)
cv2.imshow('Sobel Vertical', sobel_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()
