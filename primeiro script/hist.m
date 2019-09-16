function retorna = histograma(imagem)
    retorna = zeros(256,1);                         %cria vetor para histograma
    for i=1:length(imagem(:,1))
        for j=1:length(imagem(1,:))
            for k=1:256
                if imagem(i,j) == k-1
                    retorna(k,1)=retorna(k,1)+1;    %preenche o vetor de histograma                      
                end
            end
        end
    end
end