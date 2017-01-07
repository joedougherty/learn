"""

Looks like you can *always* name args at call time, even if they are positional.

"""

def func(arg_one, arg_two):
    print('arg_one: {}'.format(arg_one))
    print('arg_two: {}'.format(arg_two))
    return (arg_one, arg_two)

assert func(1,3) == func(arg_two=3, arg_one=1)

"""
Likewise, you can set defaults for keyword ags
"""

def func_the_greater(arg_one, arg_two, arg_three=5):
    print('arg_one: {}'.format(arg_one))
    print('arg_two: {}'.format(arg_two))
    return (arg_one, arg_two, arg_three)

assert func_the_greater(1,3) == func_the_greater(1,3, arg_three=5)

