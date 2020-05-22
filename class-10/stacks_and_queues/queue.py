from collections import deque

class Queue():
    def __init__(self):
        self.storage = deque() 
    def enqueue(self, item):
        self.storage.appendleft(item) #O(1)
    def dequeue(self):
        return self.storage.pop()
    def peek(self):
        return self.storage[-1]
    def is_empty(self):
        return len(self.storage)==0
