clc;
clear;
img             =  imread('einstein.pgm');
imgN            =  negative(img);
imgL            =  logaritmo(img,30);
imgLN           =  normali(imgL);
imgP            =  powerLaw(img,2,0.01);
imgPN             =  normali(imgP);

figure
subplot(2,3,1)
    imshow(img)
    title('imagem original')
subplot(2,3,2)
    imshow(imgN)
    title('imagem em Negativo')
subplot(2,3,3)
    imshow(uint8(imgL))
    title('imagem em logaritmico')
subplot(2,3,4)
    imshow(uint8(imgP))
    title('imagem em lei de potencia')
subplot(2,3,5)
    imshow(imgPN)
subplot(2,3,6)
    imshow(imgLN)