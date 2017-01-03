"""
When writing helper functions, prefer raising exceptions
over returning None and expecting calling function to
divine the meaning of None in that context.
"""

# Don't do this! 
def add(first_num, second_num):
    try:
        return first_num + second_num
    except TypeError: 
        # If either first_num or second_num turns
        # out to not be an int
        return None

# Rather, do this!
def add(first_num, second_num):
    try:
        return first_num + second_num
    except TypeError as e:
        raise ValueError('Both first_num and second_num must be ints!') from e

# Even *better*!
def add(first_num, second_num):
    """ 
    Adds the first_num to second_num and returns that value.
    
    In the event that either args are of the incorrect type, this
    function raises ValueError.
    """
    try:
        return first_num + second_num
    except TypeError as e:
        raise ValueError('Both first_num and second_num must be ints!') from e
