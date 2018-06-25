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
