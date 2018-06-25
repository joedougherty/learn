Atoms
=====

Any sequence of characters that starts with a lower case letter and contains letter, numbers, and the underscore is an atom.

By convention, atoms_are_all_lower_separated_by_underscores.

Variables
=========

* Start with a capital letter (A, Bc, BC, AVariable, CamelCaseVar).

* _ is the anonymous variable. 

* Singletons
    variables starting with _<upper case letter> like _Abacus are named singletons. 
    They act like normal variables, but if they only appear once they are not reported as singletons. 
    This notation is more readable sometimes than a long series of underscores.
