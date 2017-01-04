import types

# Some preliminary setup
#
# First, I'll compare two methods of creating an iterable
# from the words.txt file

# List comprehension -- does it all at one shot
with open('../supporting_materials/words.txt') as words:
    all_words = [w.strip() for w in words.readlines()]

# Generator style

# TODO: verify this works as expected. How???
# I think the real q is: 
#   * does calling readlines() just iterate over the whole file?
with open('../supporting_materials/words.txt') as words:
    all_words_gen = (w.strip() for w in words.readlines())

assert type(all_words) == list
assert type(all_words_gen) == types.GeneratorType

def len_gen(list_or_gen_of_words):
    for word in list_or_gen_of_words:
        yield len(word)

assert next(len_gen(all_words_gen)) == 1 
assert next(len_gen(all_words_gen)) == 3
assert next(len_gen(all_words_gen)) == 4 

