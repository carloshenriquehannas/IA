%Aluno 1: Carlos Henrique Hannas de Carvalho, nº USP: 11965988
%Aluno 2: Gabriel Franceschi Libardi, nº USP: 11760739.
%Atividade de listas em PROLOG

%Encontrar o primeiro elemento de uma lista
primeiro_elemento([X|_], X).    %Armazena em X, a cabeca da lista

%Encontrar o ultimo elemento de uma lista
ultimo_elemento([X], X).
ultimo_elemento([_|Z], X):-     %Percorre a cauda
    ultimo_elemento(Z, X).      %Armazena em X, o ultimo elemento da cauda

%Retirar os elementos, com mais de uma ocorrencia, da lista

%Encontrar o maior elemento da lista

%Quicksort