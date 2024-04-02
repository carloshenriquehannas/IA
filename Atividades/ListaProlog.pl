%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Exercicio 4 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Fatos: ha viagem de onibus partindo de (origem, destino)
onibus(araraquara, saocarlos).
onibus(barretos, franca).
onibus(bauru, botucatu).
onibus(botucatu, sorocaba).
onibus(franca, ribeirao).
onibus(marilia, bauru).
onibus(ribeirao, araraquara).
onibus(saocarlos, bauru).

%Regras: viagem entre uma origem e um destino, com ou sem paradas
viagem_entre(Origem, Destino):-                                 %Caso em que ha viagem direta
    onibus(Origem, Destino), !;                                 %Viagem de ida
    onibus(Destino, Origem).                                    %Viagem de volta

viagem_entre(Origem, Destino):-                                 %Caso em que ha cidade(s) intermediaria(s)
    onibus(Origem, Parada), viagem_entre(Parada, Destino), !;   %Viagem de ida com paradas 
    onibus(Destino, Parada), viagem_entre(Parada, Origem).      %Viagem de volta com paradas

%Utilizou-se o corte para que nao houvesse resposta repetida quando ha viagem de ida e volta

