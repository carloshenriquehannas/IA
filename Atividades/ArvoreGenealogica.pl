%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Fatos %%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

fem(dh).
fem(hh).
fem(me).
fem(vh).
fem(cp).
fem(so).
fem(mc).

masc(ca).
masc(ch).
masc(lg).
masc(al).
masc(lh).
masc(hs).
masc(wc).
masc(jc).
masc(mv).

progenitor(dh, ch).
progenitor(dh, lg).
progenitor(dh, hh).
progenitor(ca, ch).
progenitor(ca, lg).
progenitor(ca, hh).

progenitor(me, lh).
progenitor(me, hs).
progenitor(al, lh).
progenitor(al, hs).

progenitor(vh, dh).
progenitor(vh, me).
progenitor(wc, dh).
progenitor(wc, me).

progenitor(cp, ca).
progenitor(cp, mv).
progenitor(jc, ca).
progenitor(jc, mv).

progenitor(so, mc).
progenitor(mv, mc).

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
    Irmao1 \= Irmao2,
    !.

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
