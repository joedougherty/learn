"""
The scenario is this:

You're writing a function that takes an iterable as an argument.
You may need to iterate over said iterable multiple times,
but would not be able to do so if it were a generator.

Solution: implement the iterator protocol!

`for v in iterable_thing`
    really calls...
`iter(iterable_thing)`
    which is just another way of saying...
`iterable_thing.__iter__()`
    that method needs to return an iterator object,
    which needs to provide the __next__ method

"""

class FileReader():
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def __iter__(self):
        with open(self.path_to_file) as f:
            for line in f:
                yield line

"""
A key distiction here is between *container types* and *iterators*

When iter() receives a container type:
    returns a new iterator object each time
    (Examples: list, string, set)

When iter() receives an iterator:
    returns the iterator itself
    (Examples: generator)

Thus, you can check at runtime if a given iterable is a container 
or an iterator by calling iter() on it and seeing what it returns!
"""

# TODO: Add code to demonstrate previous block

# More on container types: 
#   https://stackoverflow.com/questions/11575925/what-exactly-are-containers-in-python-and-what-are-all-the-python-container

# See also: 
#   https://leanpub.com/intermediatepython/read#leanpub-auto-iterators-and-generators

"""
GLOSSARY:

    iterable: any type that can be used in a for loop
        ex: lists, tuples, dicts, sets

    iterator: object that implements the iterator protocol
        ex: fr = FileReader('/path/to/some/file.txt')

An iterable is *not necessarily* an iterator

iterators *must* have a __next__ method.

"""
