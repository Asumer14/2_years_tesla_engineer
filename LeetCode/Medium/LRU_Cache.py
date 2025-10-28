class LRU_Cache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None
        
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.Node(0,0)
        self.tail = self.Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    
    def _add_to_front(self, node):
        first_node = self.head.next
        node.prev = self.head
        node.next = first_node
        first_node.prev = node
        self.head.next = node

    def get(self, key:int):
        node = self.cache.get(key)

        if not node:
            return -1
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key:int, value):
        node = self.cache.get(key)

        if node:
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

            new_node = self.Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

print("--- 运行示例 ---")
cache = LRU_Cache(2)

cache.put(1, 1)
print(f"put(1, 1)")

cache.put(2, 2)
print(f"put(2, 2)")

print(f"get(1) -> {cache.get(1)}")  # returns 1

cache.put(3, 3)    # evicts key 2
print(f"put(3, 3)  # evicts key 2")

print(f"get(2) -> {cache.get(2)}")  # returns -1 (not found)

cache.put(4, 4)    # evicts key 1
print(f"put(4, 4)  # evicts key 1")

print(f"get(1) -> {cache.get(1)}")  # returns -1 (not found)
print(f"get(3) -> {cache.get(3)}")  # returns 3
print(f"get(4) -> {cache.get(4)}")  # returns 4