%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Fatos %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

fem(dione).
fem(helena).
fem(maria).
fem(vania).
fem(clelia).
fem(soraia).
fem(clara).

masc(carlos).
masc(caique).
masc(guilherme).
masc(alaim).
masc(leonardo).
masc(hermano).
masc(waldeciro).
masc(julio).
masc(kiko).

progenitor(dione, caique).
progenitor(dione, guilherme).
progenitor(dione, helena).
progenitor(carlos, caique).
progenitor(carlos, guilherme).
progenitor(carlos, helena).

progenitor(maria, leonardo).
progenitor(maria, hermano).
progenitor(alaim, leonardo).
progenitor(alaim, hermano).

progenitor(vania, dione).
progenitor(vania, maria).
progenitor(waldeciro, dione).
progenitor(waldeciro, maria).

progenitor(clelia, carlos).
progenitor(clelia, kiko).
progenitor(julio, carlos).
progenitor(julio, kiko).

progenitor(soraia, clara).
progenitor(kiko, clara).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Regras %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

pai(Pai, Filho):-
    progenitor(Pai, Filho),
    masc(Pai).

mae(Mae, Filho):-
    progenitor(Mae, Filho).
    fem(Mae).

irmaos(Irmao1, Irmao2):- %Ha repeticao de irmao porque verifica progenitor pai e mae (linha 10-15)
    progenitor(Genitor, Irmao1),
    progenitor(Genitor, Irmao2),
    Irmao1 \= Irmao2.

avos(Avo, Neto):- 
    progenitor(Avo, Filho),
    progenitor(Filho, Neto).

tios(Tio, Sobrinho):- %Ha repeticao de sobrinhos quando verificou tios. Alem disso trata apenas tios de sangue
    irmaos(Tio, Pais),
    pai(Pais, Sobrinho);
    irmaos(Tio, Pais),
    mae(Pais, Sobrinho).

primos(Primo1, Primo2):- %Ha repeticao de primos. Aparece o primo por parte de pai assim
    mae(Mae, Primo1),
    tios(Mae, Primo2).
