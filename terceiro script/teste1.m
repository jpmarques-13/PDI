clear all;clc;close all;%---Clear workspace and command window
%---Read image form the specified path and assign it to In
In = uigetfile({'*.jpg;*.tif;*.png;*.gif;*.pgm','All Image Files';'*.*','All Files' },'Select Image File');
In = imread(In);%---Read iamge and assign it to In
Ruido = imnoise(In,'salt & pepper');
Out = medfilt2(Ruido,[3 3]);
figure
imshowpair(Ruido,Out,'montage')
