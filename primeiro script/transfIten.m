clc; clear;
img =  imread('Lena.pgm');
N=length(img(1:1,:));
M=length(img(:,1:1));
img1_3=zeros(M,N);
img3_5=img1_3;
img5_7=img1_3;
img7_8=img1_3;
%histograma =imhist(img);

for i=1:M
    for j=1:N
        if img(i,j)<8
            img1_3(i,j)=img(i,j);
            img3_5(i,j)=0;
            img5_7(i,j)=0;
            img7_8(i,j)=0;
        elseif img(i,j)<32
            img1_3(i,j)=0;
            img3_5(i,j)=img(i,j);
            img5_7(i,j)=0;
            img7_8(i,j)=0;
        elseif img(i,j)<128
            img1_3(i,j)=0;
            img3_5(i,j)=0;
            img5_7(i,j)=img(i,j);
            img7_8(i,j)=0; 
        else 
            img1_3(i,j)=0;
            img3_5(i,j)=0;
            img5_7(i,j)=0;
            img7_8(i,j)=img(i,j);            
        end

    end
end
novaimg=img1_3+img3_5+img5_7+img7_8;
novaimg=uint8(novaimg);
figure
imshow(novaimg)
figure
subplot(2,2,1)
imshow(img1_3)
title('bits 1 ao 3')
subplot(2,2,2)
imshow(img3_5)
title('bits 3 ao 5')
subplot(2,2,3)
imshow(img5_7)
title('bits 5 ao 7')
subplot(2,2,4)
imshow(img7_8)
title('bit 8')
