function retorna = mediana(imagem,c)
        Out1 = medfilt2(imagem(:,:,1),[c c]);
        Out2 = medfilt2(imagem(:,:,2),[c c]);
        Out3 = medfilt2(imagem(:,:,3),[c c]);
        Out(:,:,1)=Out1;
        Out(:,:,2)=Out2;
        Out(:,:,3)=Out3;
        retorna = Out;
end