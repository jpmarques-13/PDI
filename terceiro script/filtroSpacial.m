clear all;clc;close all;%---Clear workspace and command window
%---Read image form the specified path and assign it to In
I = uigetfile({'*.jpg;*.tif;*.png;*.gif','All Image Files';'*.*','All Files' },'Select Image File');
In = imread('ruido.jpg');%---Read iamge and assign it to In

%% Filtro Gaussiano
filtro = fspecial('gaussian',[5 5],1);
Out = imfilter(In,filtro,'replicate');
figure
imshowpair(In,Out,'montage')
title('filtro gaussiano')

%% Filtro m�dia
filtro = fspecial('average',[3 3]);
for c = 1:3
Out = imfilter(In,filtro,'replicate');
end
figure
imshowpair(In,Out,'montage')
title('filtro media')

%% Filtro mediana
Out=mediana(In,3);
figure 
imshowpair(In,Out,'montage')
title('filtro mediana')

%% Melhor setup

Out = mediana(In,3);
filtro = fspecial('gaussian',[5 5],1);
Out = imfilter(Out,filtro,'replicate');
figure
imshowpair(In,Out,'montage')
title('melhor setup')


