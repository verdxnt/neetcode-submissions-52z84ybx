class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # dictionary key => the Node

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node): 
        #adds a node right after the head
        #(most recently used position)
        #<--highest priority----------lowest priority-->

        nextNode = self.head.next
        self.head.next = node
        node.next = nextNode
        node.prev = self.head
        nextNode.prev = node

    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode



    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #remove and delte the least recently used
            #-> remove form linked list and delete from hashmap
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
        
"""
    LRUCahce ->  initializes the size capacity of LRU cache

    get (int key) -> returns the key's value
            if the key doesnt exist -> return -1

    put (int key, int value) -> updates the value of the key if it exist
        if the value of the key doesnt exist -> add the vey and value pair to the cache

    if adding any key value pair cache exceed its capacity
        find the least used key and remove it

    core logic:
        cache -> is a pair of {key, value}
            so if the number of {key, value} exceeds capacity:
                -> then i need to remove the leat recelyt used key
                
        
        ------------------------------------------------------------
        --PUT()--
        -how im going to put the value:"
            -> i need to check if that key already exist
                -> if it exist -> updates ther value

        -how im going ot update the value of the key if it exsit

        -how im going ot put key-value to the cache
            every time i add a new cache {key, value} pair:
                -> i count it for that specific key

        
        - how will i keep track of the counts for each key?
          - hashmap

        -how im going to remove the least recently used key when adding a new key-value pair exceeds the LRU cache
            i will get the least recently used key from the counting i have done for each key i go though
                hashmap maybe?
        -------------------------------------------------------------

        -how im going to have to figure out how many times a key has been used
            -> key is used if:
                -> get or a put is called on it

                this means that when i call the function get/put(), i will need to make a counter that count how many times 
                its been called on that specifc key.

"""