"""
List comprehensions can create a whole new list (obviously).

A potential downside is that a list comprehension that processes
every line of an incoming file (for example) will need to read the
whole file in advance before beginning the process.

Generators defer making additional reads ahead until absolutely necessary,
so they can be more memory-efficient.
"""

# Reading a file in, generator style
all_the_words = (w.strip() for w in open('../supporting_materials/words.txt'))

# Prints the first 5 words from the dict file using a generator
for i in range(0,5):
    print(next(all_the_words))

# Generator expressions can also be composed together
lowercase_words_gen = ((w, w.lower()) for w in all_the_words)

for i in range(0,5):
    print(next(lowercase_words_gen))

