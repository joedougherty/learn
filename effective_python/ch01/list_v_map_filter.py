"""
Prefer list comprehensions over map
"""

natural_nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

negative_counter_parts = [n * -1 for n in natural_nums]

assert negative_counter_parts == [0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18]

"""
Likewise, list comprehensions can also be used in place of filter
"""

odds = [n for n in natural_nums if n % 2 != 0]

assert odds == [1,3,5,7,9,11,13,15,17]

"""
Dictionaries and sets are also capable of comprehension expressions!
"""

# A dictionary comprehension can be used to create an inverted
# dict 
#
# Example:
# Assume we have a dict where: 
#   k: letter of alphabet
#   v: numeric index of letter in alphabet
alphabet_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}

# Invert the given dict so that we end up with:
#   k: numeric index of letter in alphabet
#   v: letter of alphabet
inverted_alphabet_dict = {index: letter for letter, index in alphabet_dict.items()}

assert inverted_alphabet_dict == {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}


