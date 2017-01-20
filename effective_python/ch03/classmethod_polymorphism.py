import os
import Thread

class InputData(object):
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result

"""
How does one manage the orchestration?
"""


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    return [LineCountWorker(i) for i in input_list]


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


def mapreduce_first_pass(data_dir):
    """
    More concisely:

    return execute(create_workers(generate_inputs(data_dir)))
    """
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)

"""
So what's so bad about this?
    * PathInputData is a hard dependency in generate_inputs()
    * LineCountWorker is a hard dependency in create_workers()

It is a _version_ of mapreduce, but too specific.

The eventual goal is to be able to do this:
"""


def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)

"""
To be able to use this, we need:
    * The worker class to expose a class method (create_workers) that will
        handle the creation of the requisite worker instances
    * The input class to expose a class method (generate_inputs) that will
        handle the creation of the requisite input instances
        (called by create_workers)
"""


class GenericWorker(object):
    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result

"""
    workers = worker_class.create_workers(input_class, config)

When this line is called, the following occurs:

    * The create_workers classmethod is called
        The concrete classes in question here are:
            * LineCountWorker
            * PathInputData

    * The generate_inputs classmethod is called (with config dict)
        Assume the path given by the config dict contains 3 files:
            * a.txt
            * b.txt
            * c.txt

        generate_inputs yields a generator object that produces
        instances of the PathInputData class, one per file found
        in directory given by config dict

    * A worker is created for each input [cls(input_data)] and a list
        of all workers is returned

    * Lastly, execute fires up a thread per worker, and returns
        the accumulated results of the map calls

"""
