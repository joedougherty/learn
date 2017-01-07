"""

If you're going to use *args in a function definition, 
make sure the * is not applied to a generator, as that 
will be iterated over until it is exhausted.

Secondarily, you need to consider that if you add add'l
positional arguments, the callers of said function will 
need to take the change into account.

HOWEVER, they likely won't just explode as, after all, 
the whole idea is to accept an arbitrary number of
args.

"""

# BONUS
def command_parser(cmd, *bunch_of_args):
    print('CMD: {}'.format(cmd))
    print('ARGS: {}'.format(' '.join([a for a in bunch_of_args])))

# You already knew you could call it this way
command_parser('bludgeon', 'enemy_one', 'enemy_two')

# You can also do this!
cmd = 'bludgeon'
whole_slew_of_addl_args = ['enemy_one', 'enemy_two', 'enemy_three']

command_parser(cmd, *whole_slew_of_addl_args)

