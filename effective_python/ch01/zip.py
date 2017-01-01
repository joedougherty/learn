"""
zip is a built-in that can be used to wrap a generator around
two (or more!) iterators
"""

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

zip(letters, numbers) 

assert next(zip(letters, numbers)) == ('a', 1)

""" 
You really want to know that all applicable iterators
will have the same length ahead of time
"""

def can_safely_zip(*args):
    lengths = set([len(a) for a in args])
    return len(lengths) == 1
    
# BONUS #
# You can zip up two lists and pass them to dict

assert dict(zip(letters, numbers)) == {'a': 1, 'b': 2, 'c': 3}

