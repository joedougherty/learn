# Slide 27
def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.__next__()
        return cr

    return start


# Slide 29
@coroutine
def grep(pattern):
    print("Looking for %s" % pattern)
    try:
        while True:
            line = yield
            if pattern in line:
                print(line,)
    except GeneratorExit:
        print("Going away. Goodbye")


# Slide 38
import time
def follow(the_file, target):
    the_file.seek(0,2)
    while True:
        line = the_file.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


@coroutine
def printer():
    while True:
        line = (yield)
        print(line,)

# Slide 41
@coroutine
def grep(pattern, target):
    while True:
        line = (yield)        
        if pattern in line:
            target.send(line)
