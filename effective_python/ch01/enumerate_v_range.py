"""
Use enumerate to obtain both the value and the index 
of an iterable at every step
"""

# Rather than this...
pizza_toppings = ['mushroom', 'onion', 'black olive', 'green pepper']

for i in range(len(pizza_toppings)):
    print(i, pizza_toppings[i])

# Do this...
for idx, topping in enumerate(pizza_toppings):
    print(idx, topping)

### BONUS FACT ###
# You can set the number to start counting from 
# by specifying that int as the second param to enumerate
for idx, topping in enumerate(pizza_toppings, 100):
    print(idx, topping)

