import cv2

# Cargamos la imagen en color
img = cv2.imread("Tema_4.3/Sources/Perro.png")

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Convertimos a escala de grises
img_gris = cv2.cvtColor(img_reducida, cv2.COLOR_BGR2GRAY)

# Aplicamos el detector de bordes Canny
canny = cv2.Canny(img_gris, 50, 240)

# Mostramos las imágenes
cv2.imshow('Original reducida', img_reducida)
cv2.imshow('Canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
