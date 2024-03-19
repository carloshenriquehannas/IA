%Aluno 1: Carlos Henrique Hannas de Carvalho, nº USP: 11965988
%Aluno 2: Gabriel Franceschi Libardi, nº USP: 11760739.
%Atividade de listas em PROLOG

%Encontrar o primeiro elemento de uma lista
primeiro_elemento([X|_], X).   

%Encontrar o ultimo elemento de uma lista
ultimo_elemento([X], X).
ultimo_elemento([_|Z], X):-     
    ultimo_elemento(Z, X).      

%Retirar os elementos, com mais de uma ocorrencia, da lista

%Encontrar o maior elemento da lista. DANDO ERRO
maior_elemento([X], X).
maior_elemento([Y|Resto], X):-
    	Y > X:-
    		maior_elemento(Y, X).

%Quicksort