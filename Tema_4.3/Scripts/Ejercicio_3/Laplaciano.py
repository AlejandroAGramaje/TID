import cv2

# Cargamos la imagen en color
img = cv2.imread("Tema_4.3/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Convertimos a escala de grises
img_gris = cv2.cvtColor(img_reducida, cv2.COLOR_BGR2GRAY)

# Aplicamos el filtro Laplaciano
laplaciano = cv2.Laplacian(img_gris, cv2.CV_64F)

# Mostramos las imágenes
cv2.imshow('Original reducida', img_reducida)
cv2.imshow('Laplaciano', laplaciano)
cv2.waitKey(0)
cv2.destroyAllWindows()
