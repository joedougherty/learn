"""
If you're going to use try/except/finally blocks, 
learn how to use all the sections properly!
"""

# finally always runs
f = open('/path/to/file.txt')

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


