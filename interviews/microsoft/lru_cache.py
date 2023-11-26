"""
Interview 1:

Implement LRU Cache
"""


class LRUCache:
    def __init__(self, size=10):
        self._dll = DLL()
        self._cache = {}
        self.limit = size

    def put(self, key, value):
        if self._dll.size < self.limit:
            if key in self._cache:
                self._dll.remove_node(self._cache[key][0])

            self._dll.add_node((key, value))
            self._cache[key] = (self._dll.tail, value)
        else:
            # remove least recently used node
            del self._cache[self._dll.head.data[0]]
            self._dll.remove_node(self._dll.head)
            self.put(key, value)

    def get(self, key):
        if key in self._cache:
            node, value = self._cache[key]
            self._dll.remove_node(node)
            self._dll.add_node((key, value))
            self._cache[key] = (self._dll.tail, value)
            return value
        else:
            return None


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_node(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.size += 1

    def remove_node(self, node):
        if self.size == 1:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        del node
        self.size -= 1


if __name__ == '__main__':
    # Test LRU Cache Implementation
    cache = LRUCache(3)
    cache.put('a', 1)
    cache.put('b', 2)
    cache.put('c', 3)
    print(cache.get('a'))
    cache.put('d', 4)
    print(cache.get('b'))
    print(cache.get('c'))
    print(cache.get('d'))
    cache.put('e', 5)
    print(cache.get('a'))
    print(cache.get('b'))
    print(cache.get('c'))
    print(cache.get('d'))
    print(cache.get('e'))
