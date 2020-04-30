import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('chacra2.png')

#Mostramos la imagen original
#cv2.imshow('oring', img)
#cv2.waitKey(0)

#Obtenemos el largo y ancho
height = np.size(img, 0)
width = np.size(img, 1)

#Obtenemos el histograma
#color = ('b','g','r')
#for i, c in enumerate(color):
#    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
#    plt.plot(hist, color = c)
#    plt.xlim([0,256])
##Muestra el histograma
#plt.show()

#Aqui modificamos la imagen
for i in range (width-1):
    for j in range (height-1):
        b,g,r=img[j,i]
        #Aqui damos el umbral que querramos
        if(b<168 and b>130 and g>160 and g<200 and r>191 and r <237):
            temp=255
        else:
            temp=0
        img[j,i]=temp


cv2.imshow('cosechas de trigo', img)
cv2.waitKey(0)

cv2.destroyAllWindows()