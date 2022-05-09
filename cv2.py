#Librería o Clases
#Metodo Estatico
import cv2

#Metodo Dinamico
import numpy as np

#Tamaño de la ventana en pixeles
bgr=np.zeros((300,300,3),dtype=np.uint8)

#Color de la ventana
bgr[:,:,:]=(0,255,255)

#Mostrar la ventana
cv2.imshow('BGR',bgr)

#Esperar pulsacion de tecla
cv2.waitKey(0)

#Cerrar ventana
cv2.destroyAllWindows()