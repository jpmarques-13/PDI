import numpy as np
import cv2
from matplotlib import pyplot as plt
import os
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D


def filter(path,d1,d2):
    listing = os.listdir(path)                                                  #salva caminho das imagens de tese na variavel listing
    N = len(listing)                                                            #calcula o numero de imagens de teste
    u = np.ones((N,1))                                                          #peso igualitario a todas as imagens ( um vetor de "ums")
    sumFT = np.zeros((d1*d2,1))                                                 #vetor responsavel por armazenar a soma das PSD's das imagens
    X = np.zeros((d1*d2,N))                                                     #vetor responsavel por armazenar as FFT's das imagens
    i = 0                                                                       #contador
    for file in listing:
        curri = cv2.imread(path+file,0)                                         #lendo cada imagem na variavel curri
        if curri is None:
            pass
        else:
            curri = cv2.resize(curri,(64,64))                                       #ajustando tamanho da imagem(para facilitar o calculo)
            currFFT = np.fft.fft2(curri)                                 #calculando FFT
            X[:,i] = currFFT.flatten()                                              #armazenando FFT's no vetor X
            sumFT = sumFT + np.abs(currFFT.reshape((d1*d2,1)))**2                   #salvando PSD's na variavel sumFt
        i = i+1
    avgFT = sumFT/N                                                             #calculando PSD medio de todas as imagens
    D = np.diag((avgFT.flatten()))                                              #criando matriz D
    Di = np.linalg.inv(D)                                                       #criando matrix D inversa
    XDX = np.linalg.pinv(np.matmul(np.conj(np.transpose(X)),np.matmul(Di,X)))   #calculando produto matricial X+*Din*X
    hr = np.matmul(np.matmul(np.matmul(Di,X),XDX),u)                            #calculando filtro   Din*X*XDX*u
    h = hr.reshape((d1,d2))                                                     #ajustando filtro em forma matricial
    return h


def recognition(path,filtro,d1,d2):
    I = cv2.imread(path,0)                                                      #lendo imagem a ser testada
    if I is None :
        g=filtro*0
    else:
        I = cv2.resize(I,(d1,d2))                                                   #reajustando tamanho da imagem
        im = np.fft.fft2(I)                                                         #calculando FFT da imagem de teste
        G = im*np.conj(filtro)                                                      #calculando correlacao no dominio da frequencia
        g = np.fft.ifft2(G)                                                         #calculando correlacao no dominio espacial
        g = np.real(g)*d1*d2                                                        #coletando valores positivos
    return g
