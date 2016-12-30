"""
List comprehensions can be nested

But as a general rule, try to avoid nesting more
than two levels deep
"""

nested_tuples = [(1,2,3), (4,5,6), (7,8,9)]
flattened = [n for tup in nested_tuples for n in tup]

assert flattened == [1,2,3,4,5,6,7,8,9]

# Try to avoid more complex constructions
# Example:
flattened_odds = [n for tup in nested_tuples for n in tup if n % 2 != 0]

assert flattened_odds == [1,3,5,7,9]

