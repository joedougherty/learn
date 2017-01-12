"""

This one is effectively just ch02/closures.py all over again.

If you need to pass a callback function to a function, you can
use the __call__ method on a class to:
    * treat it as a callable 
    * maintain state inside that callable without resorting to closures + nonlocal

"""

from collections import defaultdict

class CallableCounter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return 0

statefulcounter = CallableCounter()

toppings_votes = {'pepperoni': 12, 'mushrooms': 6, 'anchovies': 1}

d = defaultdict(statefulcounter, toppings_votes)

for k, v in [('anchovies', 1), ('onions', 7)]:
    d[k] += v

assert statefulcounter.count == 1 # Onions!

