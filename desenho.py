import cv2
import numpy as np

canvas = np.ones((600, 800, 3))
cv2.imshow("Canvas", canvas)

# a)	Uma linha reta;
azul = (255, 0, 0)
cv2.line(canvas, (800, 50), (0, 50), azul)
cv2.imshow("Canvas", canvas)

# b)	Um círculo
preto = (0, 0, 0)
cv2.circle(canvas, (130, 230), 50, preto)
cv2.imshow("Canvas", canvas)

# c)	Um retagulo;
verde = (0, 255, 0)
cv2.rectangle(canvas, (10, 70), (90, 190), verde)
cv2.imshow("Canvas", canvas)

# d)	Um círculo dentro de um retangulo;
verde = (0, 255, 0)
cv2.rectangle(canvas, (272, 402), (190, 290), verde)
cv2.imshow("Canvas", canvas)

preto = (0, 0, 0)
cv2.circle(canvas, (222, 340), 26, preto)
cv2.imshow("Canvas", canvas)


# e)	A representação de um caminhão utilizando circulos, quadrados e retangulos.
# rodas
# traseira
preto = (0, 0, 0)  # x  y       tamanho
cv2.circle(canvas, (349, 525), 25, preto, -1)
# dianteira
cv2.circle(canvas, (550, 525), 25, preto, -1)

# carreta
vermelho = (0, 0, 255)
# Ini desenho altura e largura (510), (530)
# altura x e y  coordenadas(3150)  (430)
cv2.rectangle(canvas, (315, 510), (530, 380), vermelho, -1)

# cabine
cv2.rectangle(canvas, (600, 510), (531, 437), preto, -1)
# janela
cv2.rectangle(canvas, (585, 475), (547, 445), azul, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
