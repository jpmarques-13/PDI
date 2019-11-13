from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np

#PRESENÇA DE ARTEFATOS SE DÁ AO UTILIZAR JANELA RETANGULAR. 
#AS MAIS ULTILIZADAS SÃO GAUSSIANAS

#Operando com a biblioteca OPENCV

img = cv2.imread('relogio.pgm',0)
img = np.float32(img)
dft = cv2.dft(img,flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Imagem de entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Espectro original'), plt.xticks([]), plt.yticks([])
plt.show()


# Aplicando Filtros RETANGULARES
# PASSA BAIXA
rows, cols = img.shape
crow,ccol = rows/2 , cols/2

# create a mask first, center square is 1, remaining all zeros
mask_PB = np.zeros((rows,cols,2),np.uint8)
mask_PB[int(crow)-30:int(crow)+30, int(ccol)-30:int(ccol)+30] = 1

# apply mask and inverse DFT
fshift_PB = dft_shift*mask_PB
f_ishift_PB = np.fft.ifftshift(fshift_PB)
img_back_PB = cv2.idft(f_ishift_PB)
img_back_PB = cv2.magnitude(img_back_PB[:,:,0],img_back_PB[:,:,1])

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Imagem original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back_PB, cmap = 'gray')
plt.title('Filtro passa baixa'), plt.xticks([]), plt.yticks([])

plt.show()

#FILTRO PASSA ALTA

# apply mask and inverse DFT
fshift_PA = dft_shift*(1-mask_PB)
f_ishift_PA = np.fft.ifftshift(fshift_PA)
img_back_PA = cv2.idft(f_ishift_PA)
img_back_PA = cv2.magnitude(img_back_PA[:,:,0],img_back_PA[:,:,1])

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Imagem de entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back_PA, cmap = 'gray')
plt.title('Filtro passa alta'), plt.xticks([]), plt.yticks([])

plt.show()


#Filtros circulares

# Máscara circular passa baixa, centro 1, restante = 0.
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)

mask = np.zeros((rows, cols, 2), np.uint8)
r = 80
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
mask[mask_area] = 1

# Aplicando máscara e fft inversa
fshift = dft_shift * mask

fshift_mask_mag = 2000 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Imagem de entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Espectro original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(fshift_mask_mag, cmap='gray')
plt.title('Espectro + máscara'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(img_back, cmap='gray')
plt.title('Imagem após filtragem'), plt.xticks([]), plt.yticks([])
plt.show()


#Aplicando filtro passa alta circular. 1 - passa baixa

# Aplicando máscara e fft inversa
fshift = dft_shift * (1-mask)

fshift_mask_mag = 2000 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Imagem de entrada'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Espectro original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(fshift_mask_mag, cmap='gray')
plt.title('Espectro + máscara'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(img_back, cmap='gray')
plt.title('Imagem após filtragem'), plt.xticks([]), plt.yticks([])
plt.show()




#CIRCULAR PASSA FAIXA
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)  # center

# Máscara passa-faixa, 1 entre os raios definidos, 0 restante.
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)

mask = np.zeros((rows, cols, 2), np.uint8)
r_out = 70
r_in = 5
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]

mask_area = np.logical_and(((x - center[0]) ** 2 + (y - center[1]) ** 2 >= r_in ** 2),
                           ((x - center[0]) ** 2 + (y - center[1]) ** 2 <= r_out ** 2))
mask[mask_area] = 1

# Aplicando máscara e FFT inversa
fshift = dft_shift * mask

fshift_mask_mag = 2000 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Espectro original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(fshift_mask_mag, cmap='gray')
plt.title('Espectro + máscara'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(img_back, cmap='gray')
plt.title('Imagem após filtragem'), plt.xticks([]), plt.yticks([])
plt.show()