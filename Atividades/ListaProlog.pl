% Exercicio 4

%Fatos: ha viagem de onibus partindo de (origem, destino)
onibus(araraquara, saocarlos).
onibus(barretos, franca).
onibus(bauru, botucatu).
onibus(botucatu, sorocaba).
onibus(franca, ribeirao).
onibus(marilia, bauru).
onibus(ribeirao, araraquara).
onibus(saocarlos, bauru).

%Regras: viagem entre uma origem e um destino, com 0 ou mais cidades intermediarias
viagem_entre(Origem, Destino):-
    onibus(Origem, Destino).                                %Caso em que ha viagem direta
viagem_entre(Origem, Destino):-
    onibus(Origem, Parada), viagem_entre(Parada, Destino).  %Caso em que ha cidade(s) intermediaria(s)
    