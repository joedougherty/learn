( Quizzie 2-c )

: 2c-1   ( a b c --> c b a )    swap rot ;

\ "over" sans over
: 2c-2   ( x y --> x y x )      swap dup rot swap ;    

\ "not" rot
: 2c-3   ( a b c --> c a b )    swap rot swap ; \ shorter: 2c-1 swap ;
