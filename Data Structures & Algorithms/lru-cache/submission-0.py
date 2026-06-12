class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    # hash map --> quickly find a node by its key in O(1)
    # doubly linked list --> quickly move nodes to the most recently
        # used position and remove the least recently used node from the other end in O(1)

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # hash map: key --> node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        # skip over the node by pointing its previous node to its next node
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cache: # if we've seen the key in the map
            self.remove(self.cache[key]) # remove the node
            self.insert(self.cache[key]) # move it to the right
            return self.cache[key].val # return the value
        return -1 # if it doesn't exist, return -1

    def put(self, key: int, value: int) -> None:
        # update the value of the key if the key exists, otherwise, add the key-value pair to the cache
        # if the intro causes cache to exceed capacity, remove least recently used key (on the left)
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        
