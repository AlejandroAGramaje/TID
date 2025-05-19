import cv2

# Definimos los nombres de los archivos
nombre_archivo = 'Tema_4.2/Sources/Perro.png'
nombre_salida = 'ejemplo_umbralizado.jpg'

# Cargamos la imagen en escala de grises
img = cv2.imread(nombre_archivo, cv2.IMREAD_GRAYSCALE)

# Redimensionamos la imagen a la mitad
alto, ancho = img.shape[:2]
img_reducida = cv2.resize(img, (ancho // 2, alto // 2))

# Aplicamos la umbralización adaptativa con método de la media
img_umbralizada = cv2.adaptiveThreshold(
    img_reducida, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    11, 2
)

# Guardamos la imagen umbralizada
cv2.imwrite(nombre_salida, img_umbralizada)

# Mostramos las imágenes
cv2.imshow('Imagen original reducida', img_reducida)
cv2.imshow('Imagen umbralizada (adaptativa)', img_umbralizada)

# Esperamos a que se presione una tecla y cerramos las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
