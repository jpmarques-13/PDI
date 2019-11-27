import matplotlib.pyplot as plt
import numpy as np
import cv2
from matplotlib import pyplot as plt
#from PIL import Image
from mpl_toolkits.mplot3d import Axes3D


imagem = cv2.imread('sunset.png',1)
imagem = imagem[0:400,0:400]
hRGB=np.zeros((256,3))

for d1 in range(imagem.shape[0]):
    for d2 in range(imagem.shape[1]):
        for k in range(256):
            if imagem[d1,d2,0]==k:
                hRGB[k,0]=hRGB[k,0]+1
            if imagem[d1,d2,0]==k:
                hRGB[k,1]=hRGB[k,1]+1
            if imagem[d1,d2,0]==k:
                hRGB[k,2]=hRGB[k,2]+1

plt.bar(range(256),hRGB[:,0])
plt.bar(range(256),hRGB[:,1])
plt.bar(range(256),hRGB[:,2])
plt.show()
