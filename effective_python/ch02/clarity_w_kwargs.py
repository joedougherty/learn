"""
In Py3, you can denote the end of the declaration of positional 
args and the beginning of keyword-only args using * as follows:
"""

def bunch_of_args(first_pos, second_pos, *, kwarg_one=None, kwarg_two=True):
    return None

assert bunch_of_args(1,2, kwarg_one='yes', kwarg_two=False) == None

try:
    bunch_of_args(1, 2, 'yes', False)
except TypeError as e:
    print("This doesn't fly!")

