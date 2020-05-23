class Stack():
    def __init__(self):
        self.storage = []
    def push(self, item):
        self.storage.append(item)
    def pop(self):
        if not self.is_empty():
            return self.storage.pop()
        else:
            return "empty stack"
    def is_empty(self):
        return not len(self.storage)
        # if len(self.storage) == 0:
        #     return True
        # return False
    def peek(self):
        if not self.is_empty():
            return self.storage[-1]
        else:
            return "empty stack"