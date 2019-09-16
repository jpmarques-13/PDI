function retorna = acumulada(imagem)
    retorna = zeros(256,1);                                      %cria vetor para armazena a acumulada
    histograma=hist(imagem);                                     %armazena o histograma da imagem em um vetor
    M=length(imagem(1,:))*length(imagem(:,1));                   %tamanho de pixels presente na imagem 
    for i=1:256
        for j=1:i
            retorna(i) = retorna(i)+((255)/(M))*histograma(j);  %preenche os valores da acumulada no vetor criado
        end
        if mod(retorna(i),1)<0.5
            retorna(i)=retorna(i)+1;
        end
    end
    retorna=uint8(retorna);                                      %trunca valores para números inteiros
end