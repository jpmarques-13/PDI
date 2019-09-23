function retorna = normali(imagem)
    M = length(imagem(:,1));
    N = length(imagem(1,:));
    imagem = double(imagem);
    retorna = zeros(M,N);  %cria vetor para histograma
    constante = 255*(1/ max(max(imagem)));
    for i=1:length(imagem(:,1))
        for j=1:length(imagem(1,:))
                    retorna(i,j)=imagem(i,j)*constante;    %preenche o vetor de histograma                      

        end
    end
retorna = uint8(retorna)
end