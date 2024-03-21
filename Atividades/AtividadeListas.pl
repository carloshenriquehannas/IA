%Aluno 1: Carlos Henrique Hannas de Carvalho, nº USP: 11965988
%Aluno 2: Gabriel Franceschi Libardi, nº USP: 11760739.
%Atividade de listas em PROLOG

%Encontrar o primeiro elemento de uma lista
primeiro_elemento(Elemento, [Elemento|_]).   

%Encontrar o ultimo elemento de uma lista
ultimo_elemento(Elemento, [Elemento]). %Caso em que a lista tem apenas um elemento
ultimo_elemento(Elemento, [_|Cauda]):-     
    ultimo_elemento(Elemento, Cauda).      

%Retirar os elementos, com mais de uma ocorrencia, da lista

%Encontrar o maior elemento da lista
maior_elemento(Elemento, [Elemento]) %Caso em que a lista tem apenas um elemento

%Quicksort