from mace.MACEin import filter, recognition
import numpy as np
import os
import cv2

pathTeste = "./cropped/"                                                        #caminho ate imagem a ser testada
pathTreino1 = "./bart/"                                                         #caminho ate série de imagens teste
pathTreino2 = "./lisa/"                                                         #caminho ate série de imagens teste
pathTreino3= "./homer/"                                                         #caminho ate série de imagens teste
pathTreino4 = "./marge/"                                                        #caminho ate série de imagens teste

d1 = 64                                                                         #Numero de pixels verticais para de reshape
d2 = 64                                                                         #Numero de pixels horizontais para de reshape
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
h1 = filter(pathTreino1,d1,d2)                                                  #funcao retorna o filtro h (Minimul Average Correlation Energi) Filter
h2 = filter(pathTreino2,d1,d2)
h3 = filter(pathTreino3,d1,d2)
h4 = filter(pathTreino4,d1,d2)
listing = os.listdir(pathTeste)
for file in listing:
    a = recognition(pathTeste+file,h1,d1,d2)                                     #testa o filtro na imagem e plotar o grafico
    b = recognition(pathTeste+file,h2,d1,d2)
    c = recognition(pathTeste+file,h3,d1,d2)
    d = recognition(pathTeste+file,h4,d1,d2)
    if c[0,0] >= 0.85:
        count1 = count1+1
        im = cv2.imread(pathTeste+file)
        if im is None:
            pass
        else:
            cv2.imwrite('./homerclass/'+file,im)
    elif b[0,0] >= 0.85:
        count2 = count2+1
        im = cv2.imread(pathTeste+file)
        if im is None :
            pass
        else :
            cv2.imwrite('./lisaclass/'+file,im)
    elif a[0,0] >= 0.85:
        count3 = count3+1
        im = cv2.imread(pathTeste+file)
        cv2.imwrite('./bartclass/'+file,im)
    elif d[0,0] >= 0.85:
        count4 = count4+1
        im = cv2.imread(pathTeste+file)
        if im is None :
            pass
        else:
            cv2.imwrite('./margeclass/'+file,im)
    else :
        count5 = count5+1
        im = cv2.imread(pathTeste+file)
        if im is None:
            pass
        else:
            cv2.imwrite('./estranho/'+file,im)

print(count1,count2,count3,count4,count5)
