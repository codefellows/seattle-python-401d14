from linked_list import LinkedList

class Hashmap:
    """
    This class is used to implement the hashmap in python
    It contains two methods, add and hash

    Some testing:
    >>> hashmap = Hashmap(1024)
    >>> hashmap.add('ahmad', 30)
    >>> hashmap.add('silent', True)
    >>> hashmap.add('listen', 'To me')
    >>> hashmap.add('lestin', 'Random stuff')
    >>> hashmap.add('JB', 27)
    >>> for item in hashmap.map:
    ...     if item:
    ...             item.display()
    ... 
    [['silent', True], ['listen', 'To me'], ['lestin', 'Random stuff']]
    [['ahmad', 30]]
    [['JB', 27]]
    """
    def __init__(self, size):
        self.size = size
        self.map = [None]*self.size


    def hash(self, key):
        #1. split into chars
        # key = 'ahmad'
        # ['a', 'h', 'm', 'a', 'd']
        #2. convert to ascii
        #3. add together
        total = 0
        for char in key:
            total += ord(char)
        #4. multipy by prime
        total *= 19
        #5. hashed = result%size
        hashed_key = total % self.size
        return hashed_key

    def add(self, key, value):
        hashed_key = self.hash(key)

        # if None, create an empty linked list at hashed_key index
        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()

        self.map[hashed_key].append([key, value])
