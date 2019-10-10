clear all;clc;close all;%---Clear workspace and command window
%---Read image form the specified path and assign it to In
%In = uigetfile({'*.jpg;*.tif;*.png;*.gif;*.pgm','All Image Files';'*.*','All Files' },'Select Image File');
In = imread('Lena.pgm');%---Read iamge and assign it to In
Ruido = imnoise(In,'gaussian');
Ruido = imnoise(Ruido,'salt & pepper',0.6);
Out1 = medfilt2(Ruido,[5 5]);
filter = fspecial('average');
Out1 = imfilter(Out1,filter,'replicate');
Out2 = imfilter(Ruido,filter,'replicate');
Out2 = imfilter(Out2,filter,'replicate');
figure
subplot(2,1,1)
imshowpair(Ruido,Out1,'montage')
subplot(2,1,2)
imshowpair(Ruido,Out2,'montage')