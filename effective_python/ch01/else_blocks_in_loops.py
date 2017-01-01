"""
You can technically do this:
"""

import string

for letter in string.ascii_letters:
    print(letter)
else:
    print('All out of letters!')

"""
Here, the 'All out of letters!' message gets printed
after the iterator has been exhausted.

Basically, don't bother with it unless you think
you have a *really* good use case given that it's
not esp. intuitive.
"""

