""" 
This behavior can be emulated in Python2, though there's 
no direct syntactic equivalent.
"""

def bunch_of_args_py2(first_pos, second_pos, **kwargs):
    kwarg_one = kwargs.pop('kwarg_one', None)
    kwarg_two = kwargs.pop('kwarg_two', True)
    if kwargs:
        raise TypeError('Unexpected keyword argument provided: {}'.format(kwargs))

    return None

assert bunch_of_args_py2(1, 2, kwarg_one='yes', kwarg_two=True) == None

try:
    bunch_of_args_py2(1, 2, kwarg_one='yes', kwarg_two=True, kwarg_three='something')
except TypeError as e:
    print('Caught TypeError!')
    print(e)

