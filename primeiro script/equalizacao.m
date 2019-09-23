function retorna = equalizacao(imagem)
    N=length(imagem(1,:));                              %numero de colunas da imagem
    M=length(imagem(:,1));                              %numero de linhas da imagem
    retorna = zeros(M,N);                               %cria vetor para imagem de saída
    acum = acumulada(imagem);                           %recebe os valores da acumulada e armazena em um vetor
      for i=1:M 
         for j=1:N
            for k=1:256 
                 if imagem(i,j) == k-1 
                     retorna(i,j) = acum(k);            %utilizando a acumulada para mapear a imagem de saída com base na imagem de entrada
                 end
            end
         end
      end
      retorna=uint8(retorna);                            %
end