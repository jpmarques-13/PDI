clc; clear;
img             =  imread('relogio.pgm');        %grava a imagem em forma de matriz em uma variavel (imagem de entrada)
novaimg         = equalizacao(img);              %calcula a nova imagem, fazendo a equalização de histograma (imagem de saída)
histograma      = hist(img);                     %calcula o histograma da imagem de entrada
novohistograma  = hist(novaimg);                 %calcula o histograma da imagem de saida
figure
    subplot(2,2,1)
        imshow(img)
        title('imagem de entrada')
    subplot(2,2,2)
        bar(histograma)
        %imhist(img)
        title('histograma da imagem de entrada')
    subplot(2,2,3)
        imshow(novaimg)
        title('imagem de saída')
    subplot(2,2,4)
        bar(novohistograma)
        %imhist(novaimg)
        title('histograma da imagem de saída')

 
imwrite(novaimg,'./PDI/primeiro script/saida.pgm')


