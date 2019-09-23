function retorna = logaritmo(imagem,gamma,constante)
    M = length(imagem(:,1));
    N = length(imagem(1,:));
    imagem = double(imagem);
    retorna = zeros(M,N);                           %cria vetor para histograma

    for i=1:length(imagem(:,1))
        for j=1:length(imagem(1,:))
                    retorna(i,j)=(imagem(i,j)^gamma)*constante;    %preenche o vetor de histograma                      

        end
    end

end