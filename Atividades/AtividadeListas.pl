%Aluno 1: Carlos Henrique Hannas de Carvalho, nº USP: 11965988
%Aluno 2: Gabriel Franceschi Libardi, nº USP: 11760739.
%Atividade de listas em PROLOG

%Encontrar o primeiro elemento de uma lista
primeiro([Elemento | _ ], Elemento).   

%Encontrar o ultimo elemento de uma lista
ultimo([Elemento], Elemento). %Caso em que a lista tem apenas um elemento
ultimo([ _ | Cauda], Elemento):-     
    ultimo(Cauda, Elemento).

%Soma os elementos de uma lista
soma([], 0).
soma([X| Resto], Soma) :-
    soma(Resto, RestoSoma),
    Soma is RestoSoma + X.

%Retirar os elementos, com mais de uma ocorrencia, da lista
% Caso base: lista vazia
remover_repetidos([], []).
remover_repetidos([Head | Rest], [Head | Result]) :- % Se a cabeça não é elemento da cauda, mantenha-a e continue buscando na cauda.
    \+ member(Head, Rest),
    remover_repetidos(Rest, Result).
remover_repetidos([Head | Rest], Result) :- % Se a cabeça está na cauda, ignorá-la e continuar a chamada recursiva.
    member(Head, Rest),
    remover_repetidos(Rest, Result).

% Determinar maior elemento de uma lista.
maior_elemento([X], X).
maior_elemento([Head | Rest], Max) :-
    maior_elemento(Rest, RestMax),
    (   Max = undefined ; Head > RestMax ),
    Max is Head.
maior_elemento([Head | Rest], Max) :-
    maior_elemento(Rest, Max),
    (   Max = undefined ; Head =< Max ).

%Realizar a ordenação de uma lista com o algoritmo do quicksort.
quicksort([], []).
quicksort([Pivot|Rest], Sorted) :-
    partition(Rest, Pivot, Smaller, Greater),
    quicksort(Smaller, SortedSmaller),
    quicksort(Greater, SortedGreater),
    append(SortedSmaller, [Pivot|SortedGreater], Sorted).

%Predicado que faz a partição.
partition([], _, [], []).
partition([X|Xs], Pivot, [X|Smaller], Greater) :-
    X =< Pivot,
    partition(Xs, Pivot, Smaller, Greater).
partition([X|Xs], Pivot, Smaller, [X|Greater]) :-
    X > Pivot,
    partition(Xs, Pivot, Smaller, Greater).
