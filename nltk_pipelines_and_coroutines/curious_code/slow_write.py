import time


def slow_write(from_file, to_file, pause=1):
    with open(from_file, "r") as source:
        source_lines = source.readlines()

    for line in source_lines:
        with open(to_file, "a") as dest:
            dest.write(line)
        time.sleep(pause)


slow_write("sas.log", "follow_me.log")
