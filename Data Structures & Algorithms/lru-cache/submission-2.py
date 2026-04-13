class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
        
    def insert(self, node):
        left, right = self.right.prev, self.right
        node.prev, node.next = left, right
        left.next = node
        right.prev = node

    def remove(self, node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left



    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(self.cache[key])

        if self.capacity < len(self.cache):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]        
        
