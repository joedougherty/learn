Here's sort of a weird bit from [Derek Banas' Prolog Video](https://www.youtube.com/watch?v=SykxWpFwMGs):


    % At the REPL/query prompt...

    ?- rich(money, X) = rich(Y, no_debt).

This evaluates to **true** but I'm not sure I understand what it means.


# trace #

toggle on with: `trace.`


DIG THIS
========


I'm really liking this pattern matching/overloading/recursion thing that happens. 

    % (Earlier in time)
    %
    %   ODIN
    %    ||
    %    \/
    %   SVEN
    %    ||
    %    \/
    %  JOSEPH
    %    ||
    %    \/
    %   MARK
    %    ||
    %    \/
    %   JOE
    %
    % (Later in time)

    parent_of(mark, joe).
    parent_of(joseph, mark).
    parent_of(sven, joseph).
    parent_of(odin, sven).

    ancestor_of(X, Y) :-
        parent_of(X, Y).

    ancestor_of(X, Y) :-
        parent_of(X, P),
        ancestor_of(P, Y).


TRACE A CALL!

try...

    ancestor_of(joseph, joe).

	[trace]  ?- ancestor_of(joseph,joe).
	   Call: (8) ancestor_of(joseph, joe) ? creep
	   Call: (9) parent_of(joseph, joe) ? creep
	   Fail: (9) parent_of(joseph, joe) ? creep
	   Redo: (8) ancestor_of(joseph, joe) ? creep
	   Call: (9) parent_of(joseph, _2740) ? creep
	   Exit: (9) parent_of(joseph, mark) ? creep
	   Call: (9) ancestor_of(mark, joe) ? creep
	   Call: (10) parent_of(mark, joe) ? creep
	   Exit: (10) parent_of(mark, joe) ? creep
	   Exit: (9) ancestor_of(mark, joe) ? creep
	   Exit: (8) ancestor_of(joseph, joe) ? creep
	true .

