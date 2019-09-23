function retorna = negative(imagem)
    M = length(imagem(:,1));
    N = length(imagem(1,:));
    retorna = zeros(M,N);                         %cria vetor para histograma
    for i=1:length(imagem(:,1))
        for j=1:length(imagem(1,:))
                    retorna(i,j)=255-imagem(i,j);    %preenche o vetor de histograma                      

        end
    end
    retorna = uint8(retorna);
end
