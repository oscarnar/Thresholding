import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('celulas.png')
cv2.imshow('lena', img)
cv2.waitKey(0)

height = np.size(img, 0)
width = np.size(img, 1)
#width, height = cv2.getSize(src)
img2 = np.zeros((height,width,3),np.uint8)

#Obtenemos el histograma
color = ('b','g','r')
for i, c in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])
#Muestra el histograma
#plt.show()

#Aqui modificamos la imagen para VIVAS
for i in range (width-1):
    for j in range (height-1):
        b,r,g=img[j,i]
        temp=int((b+r+g)/3)
        #Aqui damos el umbral que querramos
        if(b<=180 and b>=155):
            temp=255
        else:
            temp=1
        img2[j,i]=temp

cv2.imshow('vivas', img2)
cv2.waitKey(0)

#Aqui modificamos la imagen para MUERTAS
for i in range (width-1):
    for j in range (height-1):
        b,r,g=img[j,i]
        temp=int((b+r+g)/3)
        #Aqui damos el umbral que querramos
        if(b<=145):
            temp=255
        else:
            temp=1
        img[j,i]=temp

cv2.imshow('muertas', img)
cv2.waitKey(0)

cv2.destroyAllWindows()