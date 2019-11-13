from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np

# Leitura da imagem
img_original = cv2.imread('einsteinRuido.jpg',0) # imagem tons de cinza
img_original = img_original.astype(float)


#Aplicação de filtro da média
Tamanho_Kernel = 3
kernel = np.ones((Tamanho_Kernel,Tamanho_Kernel),np.float32)/Tamanho_Kernel*Tamanho_Kernel
img_Filtrada0 = cv2.filter2D(img_original,-1,kernel)

Tamanho_Kernel2 = 5
kernel = np.ones((Tamanho_Kernel2,Tamanho_Kernel2),np.float32)/Tamanho_Kernel2*Tamanho_Kernel2
img_Filtrada2 = cv2.filter2D(img_original,-1,kernel)

Tamanho_Kernel3 = 7
kernel = np.ones((Tamanho_Kernel3,Tamanho_Kernel3),np.float32)/Tamanho_Kernel3*Tamanho_Kernel3
img_Filtrada3 = cv2.filter2D(img_original,-1,kernel)

plt.subplot(2, 2, 1), plt.imshow(img_original, cmap='gray')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(img_Filtrada0, cmap='gray')
plt.title('Média 3x3'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(img_Filtrada2, cmap='gray')
plt.title('Média 5x5'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(img_Filtrada3, cmap='gray')
plt.title('Média 7x7'), plt.xticks([]), plt.yticks([])
plt.show()


img_original = cv2.imread('Lena.pgm',0) # imagem tons de cinza
#Aplicação de filtro da mediana
img_Filtrada4 = cv2.medianBlur(img_original,3)
img_Filtrada5 = cv2.medianBlur(img_original,5)

plt.subplot(1, 3, 1), plt.imshow(img_original, cmap='gray')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(img_Filtrada4, cmap='gray')
plt.title('Mediana 3x3'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(img_Filtrada5, cmap='gray')
plt.title('Mediana 5x5'), plt.xticks([]), plt.yticks([])
plt.show()



#Aplicação de filtro Gaussiano
img_Filtrada6 = cv2.GaussianBlur(img_original,(3,3),0,-1,0,cv2.BORDER_DEFAULT)

img_Filtrada7 = cv2.GaussianBlur(img_original,(5,5),0,-1,0,cv2.BORDER_DEFAULT)

img_Filtrada8 = cv2.GaussianBlur(img_original,(7,7),0,-1,0,cv2.BORDER_DEFAULT)
 
plt.subplot(2, 2, 1), plt.imshow(img_original, cmap='gray')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(img_Filtrada6, cmap='gray')
plt.title('Gaussiano 3x3'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(img_Filtrada7, cmap='gray')
plt.title('Gaussiano 5x5'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(img_Filtrada8, cmap='gray')
plt.title('Gaussiano 7x7'), plt.xticks([]), plt.yticks([])
plt.show()

    #OPÇÕES PARA BORDAS:
    # BORDER_CONSTANT
    # BORDER_REPLICATE
    # BORDER_REFLECT
    # BORDER_WRAP
    # BORDER_REFLECT
    # BORDER_TRANSPARENT
    # BORDER_REFLECT101
    # BORDER_ISOLATED


    #Aplicação do filtro Laplaciano
Laplaciano = cv2.Laplacian(img_original,cv2.CV_64F)    
plt.imshow(Laplaciano)
img_Filtrada = img_original + Laplaciano

plt.subplot(1,2,1)
plt.imshow(img_original,cmap='gray')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2)
plt.imshow(Laplaciano,cmap='gray')
plt.title('Laplaciano'), plt.xticks([]), plt.yticks([])
# plt.subplot(1,3,3)
# plt.imshow(img_Filtrada,cmap='gray')
# plt.title('Imagem Original + Laplaciano'), plt.xticks([]), plt.yticks([])
plt.show()



    #Aplicação do filtro de Sobel
img_Filtrada9 = cv2.Sobel(img_original,-1,2,2) #Calculando derivadas de segunda ordem!
plt.subplot(1,2,1)
plt.imshow(img_original,cmap='gray')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2)
plt.imshow(img_Filtrada9,cmap='gray')
plt.title('Sobel d2x,d2y'), plt.xticks([]), plt.yticks([])
plt.show()

# #Aplicação do filtro bilateral
# img_original = img_original.astype('float32')
# #Parâmetros: 10 - largura do filtro, 100 - Sigma color (>150)
# img_Filtrada = cv2.bilateralFilter(img_original,10,150,150)

