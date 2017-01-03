"""
If you're going to use try/except/finally blocks, 
learn how to use all the sections properly!
"""

# finally always runs
f = open('../supporting_materials/words.txt')

try:
    content = f.read()
finally:
    f.close()
    
# else blocks can be used to
# run code if the try code 
# has *not* raised an exception
try:
    assert None is None
except ValueError as e:
    raise
else:
    print('this will run as the try block here is tautological')

def give_me_nothing():
    return None

# Put it all together -- try/except/else/finally
try:
    assert give_me_nothing() == None # This will pass
    assert give_me_nothin() == None  # This will raise a NameError, though
except AssertionError as e:
    raise e
else:
    print('My `assert` in the try block must not have raised any exceptions')
finally:
    print('This *always* prints!')
