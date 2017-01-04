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

# TODO: Look more closely at class-based example 
# given on pg. 35

if __name__ == '__main__':
    import doctest
    doctest.testmod()
