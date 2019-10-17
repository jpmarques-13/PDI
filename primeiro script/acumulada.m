function retorna = acumulada(imagem)
    retorna = zeros(256,1);                                      %cria vetor para armazena a acumulada
    histograma=hist(imagem);                                     %armazena o histograma da imagem em um vetor
    M=length(imagem(1,:))*length(imagem(:,1));                   %tamanho de pixels presente na imagem 
    acumulada = zeros(256,1);                                    %cria vetor para armazena a acumulada
    acumulada = acumulada+histograma*255/M;
    retorna = tril(ones(256,256));
    retorna = uint8(ceil(retorna*acumulada));
end