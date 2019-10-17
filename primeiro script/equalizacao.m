function retorna = equalizacao(imagem)
    N=length(imagem(1,:));                              %numero de colunas da imagem
    M=length(imagem(:,1));                              %numero de linhas da imagem
    retorna = zeros(M,N);                               %cria vetor para imagem de saída
    acum = acumulada(imagem);
    retorna= acum(imagem+1);               %mapeia os valores de acumulada no imagem
end