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
    which needs to provude the __next__ method

"""

class GenericFileReaderGenerator():
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
When iter() receives an iterator:
    returns the iterator itself

Thus, you can check at runtime if a given iterable is a container 
or an iterator by calling iter() on it and seeing what it returns!
"""

# TODO: Add code to demonstrate previous block
