import pytest

# --- CLASS UNDER TEST ---

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left        

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt

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
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# --- PARAMETRIZED TEST CASES ---

@pytest.mark.parametrize("capacity, operations, expected", [
    # Basic LRU behavior
    (
        2,
        [("put", 1, 1), ("put", 2, 2), ("get", 1), ("put", 3, 3), ("get", 2), ("put", 4, 4), ("get", 1), ("get", 3), ("get", 4)],
        [-1 if op[0] == "get" and op[1] in [2, 1] else val for op, val in zip(
            [("get", 1), ("get", 2), ("get", 1), ("get", 3), ("get", 4)],
            [1, -1, -1, 3, 4]
        )]
    ),
    # Update existing key
    (
        2,
        [("put", 1, 1), ("put", 1, 10), ("get", 1), ("put", 2, 2), ("put", 3, 3), ("get", 1)],
        [10, -1]
    ),
    # Single capacity
    (
        1,
        [("put", 1, 100), ("get", 1), ("put", 2, 200), ("get", 1), ("get", 2)],
        [100, -1, 200]
    ),
    # Get nonexistent key
    (
        2,
        [("get", 999), ("put", 1, 1), ("get", 2)],
        [-1, -1]
    ),
    # Access order affects eviction
    (
        2,
        [("put", 1, 1), ("put", 2, 2), ("get", 1), ("put", 3, 3), ("get", 2), ("get", 1), ("get", 3)],
        [1, -1, 1, 3]
    )
])
def test_lru_cache(capacity, operations, expected):
    cache = LRUCache(capacity)
    output = []

    for op in operations:
        if op[0] == "put":
            cache.put(op[1], op[2])
        elif op[0] == "get":
            output.append(cache.get(op[1]))

    assert output == expected
