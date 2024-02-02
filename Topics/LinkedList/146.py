class Node:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.size = 0
        self.capacity = capacity
        self.nodes = dict()
        self.keys = dict()

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.remove_node(node)
        self.add_to_tail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self.remove_node(node)
        else:
            if self.size == self.capacity:
                head_key = self.keys[self.head]
                del self.keys[self.head]
                del self.nodes[head_key]
                self.remove_node(self.head)

            self.nodes[key] = Node(value, None, None)
            self.keys[self.nodes[key]] = key

        self.add_to_tail(self.nodes[key])


    def remove_node(self, node):
        prev = node.prev
        next = node.next

        if next:
            next.prev = prev

        if prev:
            prev.next = next

        if not prev:
            self.head = next

        if not next:
            self.tail = prev

        node.prev = None
        node.next = None

        self.size -= 1
    def add_to_tail(self, node):
        self.size += 1
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    lru_cache = LRUCache(1)
    res1 = lru_cache.put(2, 1)
    res2 = lru_cache.get(2)
    res3 = lru_cache.put(3, 2)
    print(res3)


