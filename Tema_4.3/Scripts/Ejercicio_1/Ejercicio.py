import cv2
import numpy as np
import math

# Crear lienzo general (altura fija, ancho para 3 bloques)
alto, ancho = 400, 1200
lienzo = 255 * np.ones((alto, ancho, 3), dtype=np.uint8)

# 1. Sol con picos (izquierda)
# ======================
centro = (200, 200)
radio_azul = 120
radio_amarillo = 100
radio_rojo = 80
picos = 16

# Fondo azul
cv2.circle(lienzo, centro, radio_azul, (255, 0, 0), -1)

# Estrella amarilla (con picos)
pts = []
for i in range(picos * 2):
    angulo = i * math.pi / picos
    r = radio_amarillo if i % 2 == 0 else radio_amarillo - 20
    x = int(centro[0] + r * math.cos(angulo))
    y = int(centro[1] + r * math.sin(angulo))
    pts.append((x, y))
cv2.fillPoly(lienzo, [np.array(pts, np.int32)], (0, 255, 255))  # Amarillo

# Círculo rojo interior
cv2.circle(lienzo, centro, radio_rojo, (0, 0, 255), -1)

# 2. Bandera UK (centro)
x_offset = 400  # posición horizontal de inicio
bandera = 255 * np.ones((400, 400, 3), dtype=np.uint8)

# Fondo azul
bandera[:] = (255, 0, 0)

# Cruces diagonales blancas y rojas
cv2.line(bandera, (0, 0), (400, 400), (255, 255, 255), 60)
cv2.line(bandera, (400, 0), (0, 400), (255, 255, 255), 60)
cv2.line(bandera, (0, 0), (400, 400), (0, 0, 255), 20)
cv2.line(bandera, (400, 0), (0, 400), (0, 0, 255), 20)

# Cruces centrales
cv2.rectangle(bandera, (170, 0), (230, 400), (255, 255, 255), -1)
cv2.rectangle(bandera, (0, 170), (400, 230), (255, 255, 255), -1)
cv2.rectangle(bandera, (185, 0), (215, 400), (0, 0, 255), -1)
cv2.rectangle(bandera, (0, 185), (400, 215), (0, 0, 255), -1)

# Pegar bandera al lienzo
lienzo[:, x_offset:x_offset+400] = bandera

# 3. Bloques
# ======================
x_offset = 800
mondrian = 255 * np.ones((400, 400, 3), dtype=np.uint8)

# Rectángulos de colores
cv2.rectangle(mondrian, (0, 0), (250, 250), (200, 200, 200), -1)     # gris claro
cv2.rectangle(mondrian, (250, 0), (400, 100), (0, 255, 255), -1)     # amarillo
cv2.rectangle(mondrian, (0, 250), (150, 400), (0, 255, 255), -1)     # amarillo
cv2.rectangle(mondrian, (150, 250), (250, 400), (0, 0, 0), -1)       # negro
cv2.rectangle(mondrian, (250, 100), (400, 250), (0, 0, 255), -1)     # rojo
cv2.rectangle(mondrian, (250, 250), (325, 325), (255, 255, 255), -1) # blanco
cv2.rectangle(mondrian, (325, 250), (400, 325), (255, 0, 0), -1)     # azul

# Líneas negras
cv2.line(mondrian, (250, 0), (250, 400), (0, 0, 0), 10)
cv2.line(mondrian, (0, 250), (400, 250), (0, 0, 0), 10)
cv2.line(mondrian, (150, 250), (150, 400), (0, 0, 0), 10)
cv2.line(mondrian, (325, 250), (325, 400), (0, 0, 0), 10)
cv2.line(mondrian, (250, 100), (400, 100), (0, 0, 0), 10)

# Pegar mondrian al lienzo
lienzo[:, x_offset:x_offset+400] = mondrian

# Mostrar resultado final
# ======================
cv2.imshow("Ejercicio composiciones", lienzo)
cv2.waitKey(0)
cv2.destroyAllWindows()
