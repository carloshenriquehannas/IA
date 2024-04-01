% Exercicio 4

%Declaracao de fatos: aa viagem de onibus(origem, destino)
onibus(araraquara, saocarlos).
onibus(barretos, franca).
onibus(bauru, botucatu).
onibus(botucatu, sorocaba).
onibus(franca, ribeirao).
onibus(marilia, bauru).
onibus(ribeirao, araraquara).
onibus(saocarlos, bauru).

%Regras: viagem entre uma origem e um destino. ERRO QUANDO A VIAGEM NAO EH DIRETA
viagemEntre(Origem, Destino):-
    onibus(Origem, Destino).    %Caso em que ha onibus direto
    viagem(Origem, [Origem|Caminho], [Origem|Caminho]).
    viagem(Origem, [Ultima_Cidade|Caminho_Agora], Caminho):-
        onibus(Nova_Cidade, Ultima_Cidade),
        not(pertence(Nova_Cidade, Caminho_Agora)),
        viagem(Origem, [Nova_Cidade, Ultima_Cidade|Caminho_Agora], Caminho).

pertence(Cidade, [Cidade|_]):- !.
pertence(Cidade, [_|Cidade]):- 
    pertence(Cidade, Caminho).

        




    