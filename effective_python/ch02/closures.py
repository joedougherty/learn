"""
Python3 has a `nonlocal` keyword. 
It is used to extract values from closures into 
their containing scope.
"""

def outer():
    """
    >>> outer()
    'I have not been overwritten'
    """
    pertinent_value = 'I have not been overwritten'
    def inner():
        pertinent_value = 'I *have* been overwritten!'
        return pertinent_value
    return pertinent_value

def outer_nonlocal():
    """
    >>> outer_nonlocal()
    'I *have* been overwritten!'
    """
    pertinent_value = 'I have not been overwritten'
    def inner():
        nonlocal pertinent_value
        pertinent_value = 'I *have* been overwritten!'

    inner()
    return pertinent_value

"""
In the case that you need to do this in Python2,
you can use a mutable value (val passed by reference)
"""
# By way of example
# (I *really* do not care for this)
def outer_py2():
    """
    >>> outer_py2()
    12
    """
    pertinent_value = [6]
    def inner():
        pertinent_value[0] = 12

    inner()
    return pertinent_value[0]

# Another way to do this *without* using nonlocal
# is to create a small class and use the __call__ 
# method to pass it around as though it were a function
class CustomOrderer:
    def __init__(self, haystack):
        self.haystack = haystack
        self.detected = False

    def __call__(self, needle):
        if needle in self.haystack:
            self.detected = True
            return (0, needle)
        return (1, needle)

chosen_ones = [11,13,17,19,23]
orderer = CustomOrderer(chosen_ones)
mostly_evens = [2,4,6,8,10,12,13,14,16,18,20]
mostly_evens.sort(key=orderer)

assert mostly_evens == [13,2,4,6,8,10,12,14,16,18,20]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
