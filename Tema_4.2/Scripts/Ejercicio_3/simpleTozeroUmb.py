import cv2

# Cargamos la imagen en escala de grises
img = cv2.imread("Tema_4.2/Sources/Perro.png", cv2.IMREAD_GRAYSCALE)

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Aplicamos la umbralización TOZERO
thresh, img_umbralizada = cv2.threshold(img_reducida, 128, 255, cv2.THRESH_TOZERO)

# Guardamos la imagen umbralizada
cv2.imwrite("ejemplo_umbralizado.jpg", img_umbralizada)

# Mostramos las imágenes
cv2.imshow("Imagen original reducida", img_reducida)
cv2.imshow("Imagen umbralizada (TOZERO)", img_umbralizada)

# Esperamos a que el usuario presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
