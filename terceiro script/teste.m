I = uigetfile({'*.jpg;*.tif;*.png;*.gif;*.pgm','All Image Files';'*.*','All Files' },'Select Image File');
In = imread(I);%---Read iamge and assign it to In


In = rgb2gray(In);
Y = fft2(In);

Y1 = log(1+abs(abs(fftshift(Y))));
imshow(Y1,[]);

img = uint8(ifft2(ifftshift(Y)));
imshow(In,[]);