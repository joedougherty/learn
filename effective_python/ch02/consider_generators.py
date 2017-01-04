# Some preliminary setup
#
# First, I'll compare two methods of creating an iterable
# from the words.txt file

import types

# List comprehension -- does it all at one shot
with open('../supporting_materials/words.txt') as words:
    all_words = [w.strip() for w in words.readlines()]

# Generator style
# TODO: verify this works as expected. How???
with open('../supporting_materials/words.txt') as words:
    all_words_gen = (w.strip() for w in words.readlines())

assert type(all_words) == list
assert type(all_words_gen) == types.GeneratorType

