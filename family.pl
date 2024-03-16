%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Fatos %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

fem(dione).
fem(helena).

masc(carlos).
masc(caique).
masc(guilherme).

progenitor(dione, caique).
progenitor(dione, guilherme).
progenitor(dione, helena).
progenitor(carlos, caique).
progenitor(carlos, guilherme).
progenitor(carlos, helena).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Regras %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

pai(Pai, Filho):-
    progenitor(Pai, Filho),
    masc(Pai).

mae(Mae, Filho):-
    progenitor(Mae, Filho).
    fem(Mae).

irmao(Irmao1, Irmao2):- %Ha repeticao de irmao porque verifica progenitor pai e mae (linha 10-15)
    progenitor(Genitor, Irmao1),
    progenitor(Genitor, Irmao2),
    Irmao1 \= Irmao2.