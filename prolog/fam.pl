male(joe).
male(dan).
male(chris).
male(mark).
male(joseph).
male(michael).
male(kevin).
male(paul).
male(tom).

female(monica).
female(peg).
female(marie).
female(claire).
female(denise).
female(lauren).
female(crystal).
female(mary).
female(beverly).

% Ordering:
% ========
% X is the parent of Y.
%
% Example:
% =======
% peg is the parent of joe.
parent_of(peg, joe).
parent_of(peg, dan).
parent_of(peg, chris).
parent_of(peg, monica).
parent_of(marie, tom).
parent_of(marie, mark).
parent_of(marie, kevin).
parent_of(marie, denise).
parent_of(claire, peg).
parent_of(claire, paul).
parent_of(beverly, crystal).
parent_of(paul, crystal).
parent_of(lauren, denise).
parent_of(mark, joe).
parent_of(mark, dan).
parent_of(mark, monica).
parent_of(mark, chris).
parent_of(mark, joseph).

mother_of(X,Y) :-
    female(X),
    parent_of(X,Y).

father_of(X,Y) :-
    male(X),
    parent_of(X,Y).

daughter_of(X,Y) :-
    female(X),
    parent_of(X,Y).

son_of(X,Y) :-
    male(X),
    father_of(Y,X).

siblings(X,Y) :-
    parent_of(P,X),
    parent_of(P,Y),
    X\=Y.

brother_of(X,Y) :-
    male(X),
    siblings(X,Y).

sister_of(X,Y) :-
    female(X),
    siblings(X,Y).

uncle_of(X,Y) :-
    brother_of(X,G),
    parent_of(G,Y).

cousin_of(X,Y) :-
    parent_of(P,X),
    siblings(P,Q),
    parent_of(Q,Y).




























