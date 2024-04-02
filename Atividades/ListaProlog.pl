%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Exercicio 4 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

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

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Exercicio 5 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Parte I
    %Fatos: aluno possui (nome, endereco, tel, data de nascimento, t1, p1, t2, p2, sub, rec, freq)
    aluno("Carlos Silva", "Rua Orquideas 32", "000000000", "01/01/2001", 10, 10, 10, 10, _, _, 100).
    aluno("Pedro Augusto", "Rua Orquideas 28", "222222222", "01/01/2001", 10, 10, 10, 10, _, _, 65).
    aluno("Lucas Alves", "Rua Orquideas 34", "333333333", "01/01/2003", 10, 10, 10, 10, _, _, 60).
    aluno("Joao Almeida", "Rua Orquideas 30", "111111111", "01/01/2001", 1, 4, 3, 2, _, _, 90).

    %Regras: media de provas (p1 e p2), media de trabalhos (t1 e t2)
    media_prova(Aluno, MediaProva):-                                            %Media de provas do aluno
        aluno(Aluno, _, _, _, _, P1, _, P2, Sub, _, _), 
        MediaProva is (2*P1 + 3*P2)/5.
        %PROBLEMA: media_prova() nao considera a possibilidade de sub

    media_trabalho(Aluno, MediaTrabalho):-                                      %Media de trabalhos do aluno
        aluno(Aluno, _, _, _, T1, _,T2, _, _, _, _), 
        MediaTrabalho is (1*T1 + 3*T2)/4.

    media_final(Aluno, MediaFinal):-                                            %Medial final do aluno
        media_prova(Aluno, MediaProva), media_trabalho(Aluno, MediaTrabalho),
        MediaFinal is (MediaProva + MediaTrabalho)/2.

    situacao(Aluno):-
        media_final(Aluno, MediaFinal), MediaFinal < 5, write('Reprovado'), !;  %Se media final < 5 eh reprovado
        write('Aprovado').                                                      %Senao, eh aprovado.
    
%Parte II
    %Nota 10 na P1 e P2: ?- findall(X, aluno(X,_,_,_,_, 10,_, 10, _, _, _), Gabarito).
    %Nota 10 no T1 e T2: ?- findall(X, aluno(X,_,_,_,10,_,10,_, _, _, _), Gabarito).
    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
