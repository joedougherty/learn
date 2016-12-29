import string

"""
Given a sequence, you can use the `stride` value choose only every nth 
value from the sequence in question.
"""

letters = string.ascii_lowercase

# Say we only want a,c,e,g, etc.
every_other_letter_seq = letters[::2]

assert letters[::2] == 'acegikmoqsuwy'

# What about nested sequences?
nested_jawn = [0, [1,2,3], 2, [4,5,6]]

list_of_lists = nested_jawn[1::2]

assert list_of_lists == [[1,2,3], [4,5,6]]

