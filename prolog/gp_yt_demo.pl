parent(albert, bob).
parent(albert, betsy).
parent(albert, bill).

parent(alice, bob).
parent(alice, betsy).
parent(alice, bill).

parent(bob, carl).
parent(bob, charlie).

get_grandchild :-
    parent(albert, X),
    parent(X, Y),
    format('Albert\'s grandchild is: ~s ~n', [Y]).

grandchildren_of(P) :-
    parent(P, X),
    parent(X, Y),
    format('~s\'s grandchild is: ~s. ~n', [P,Y]).

customer(joe, dougherty, 666.66).
customer(bob, smith, 0.0).

get_cust_balance(Fname, Lname) :-
    customer(Fname, Lname, Balance),
    format('~s ~s has balance: ~2f', [Fname, Lname, Balance]).

vertical(line(point(X, Y), point(X, Y2))).
horizontal(line(point(X, Y), point(X2, Y)))
