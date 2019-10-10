from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np

# Leitura da imagem
img_original = cv2.imread('einstein.pgm',0) # imagem tons de cinza
img_original = img_original.astype(float)

Filtro = input('Selecione o filtro de entrada: 1 = Filtro negativo, 2 = Filtro log e 3 = Filtro exponencial')
Filtro_INT  = int(Filtro)
if Filtro_INT == 1:
#Aplicação de filtro negativo
    img_FiltroNEG = np.max(img_original) - img_original 
    img_Filtrada = img_FiltroNEG
elif Filtro_INT == 2:

#Aplicação de filtro LOG
    img_FiltroLog = np.log(1+img_original)
    img_Filtrada = img_FiltroLog
elif Filtro_INT == 3:

#Aplicação de filtro exponencial
    img_FiltroEXP = np.array(255*(img_original/255)**.4,dtype='uint8') # Foi calculado com o gamma = 0.4
    img_Filtrada = img_FiltroEXP
else: 
    print('Escolha um filtro válido')
    exit()

#Plot
plt.subplot(1,2,1)
plt.imshow(img_original,cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(img_Filtrada,cmap='gray')
plt.axis('off')

plt.show()