clc;
clear;
img             =  imread('Lena.pgm');
imgN            =  negative(img);
imgL            =  logaritmo(img,30);
imgLN           =  normali(imgL);
imgP            =  powerLaw(img,2,0.01);
imgPN             =  normali(imgP);

    
t = linspace(0,1,100);  
figure
subplot(2,1,1)
   plot(log(t))
   title('funcao ln')
subplot(2,1,2)
    plot(t.^3)
    title('funcao gamma (gamma>0)')

    
    
figure
subplot(2,3,1)
    imshow(img)
    title('imagem original')
subplot(2,3,4)
    imshow(imgN)
    title('imagem em Negativo')
subplot(2,3,2)
    imshow(uint8(imgL))
    title('imagem em logaritmico')
subplot(2,3,3)
    imshow(uint8(imgP))
    title('imagem em lei de potencia')
subplot(2,3,6)
    imshow(imgPN)
    title('imagem em lei de potencia normalizado')
subplot(2,3,5)
    imshow(imgLN)
    title('imagem em logaritmico normalizado')