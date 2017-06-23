class Stack:
    def __init__(self):
        self.contents = []

    def push(self, item):
        self.contents.append(item)

    def pop(self):
        return self.contents.pop()

    def peek(self):
        return self.contents[-1]

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.contents)
