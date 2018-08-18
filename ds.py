"""Implementation of data structures."""

from datetime import datetime
from random import randint
import unittest


def runime_analysis(f):
    def wrapper(*args, **kwargs):
        time_fr = datetime.now()
        result = f(*args, **kwargs)
        time_to = datetime.now()
        time_diff = time_to - time_fr
        print time_diff
        return result

    return wrapper


class LinkedListNode(object):
    """Linked List Node."""

    def __init__(self, value):
        """."""
        self.value = value
        self.next = None


class DoubleLinkedListNode(object):
    """."""

    def __init__(self, value):
        """."""
        self.value = value
        self.next = None
        self.prev = None


class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class GraphNode:
    def __init__(self, value=None, neighbor=None):
        self.value = value
        self.neighbor = neighbor


class LinkedList:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.values = []

    def is_empty(self):
        return not self.values

    def peak(self):
        return self.values[-1] if self.values else None

    def pop(self):
        return self.values.pop() if self.values else None

    def push(self, value):
        self.values.append(value)

    def size(self):
        return len(self.values)


class MinHeap(TreeNode):
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        pass


class HashTable():
    pass


class struct_constant_time(object):
    """Design a data structure that supports insert, delete, search and getRandom in constant time."""
    def __init__(self):
        self.map = dict()
        self.array = list()

    def insert(self, val):
        if val not in self.map:
            self.array.append(val)
            self.map[val] = len(self.array) - 1

    def delete(self, val):
        if val in self.map:
            index = self.map[val]
            array_length = len(self.array)
            self.array[index], self.array[array_length - 1] = self.array[array_length - 1], self.array[index]
            if index != array_length - 1:
                self.map[self.array[index]] = index

            self.array.pop()
            del self.map[val]

    def search(self, val):
        return val if val in self.map else None

    def get_random(self):
        index = randint(0, len(self.array) - 1)
        return self.array[index]


class LRUCache(object):
    """."""

    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)

    def __init__(self, capacity):
        """.

        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.cache = dict()
        self.usage = dict()             # Usage usage.
        self.head = LinkedListNode()    # Least recently used cache.
        self.tail = LinkedListNode()    # Most recently used cache.

    def _update_recent_used_node(self, key):
        """."""
        node = LinkedListNode(key)
        self.tail.next = node
        self.tail = node

    def get(self, key):
        """.

        :type key: int
        :rtype: int
        """
        value = self.cache.get(key, -1)
        self._update_recent_used_node(key)
        return value

    def put(self, key, value):
        """.

        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.cache and len(self.cache.keys()) > self.capacity:
            self.cache.pop(self.head.value)
            self.head = self.head.next

        self.usage[key] = self.cache.get(key, 1)
        self.cache[key] = value
        self._update_recent_used_node(key)


class TestCaseDS(unittest.TestCase):
    """Test case for implementation of data structures."""

    def test_lru_cache(self):
        """."""
        lru_cache = LRUCache(2)
        lru_cache.put(1, 1)
        lru_cache.put(2, 2)
        self.assertEqual(lru_cache.get(1), 1)
        lru_cache.put(3, 3)
        self.assertEqual(lru_cache.get(2), -1)
        lru_cache.put(4, 4)
        self.assertEqual(lru_cache.get(1), -1)
        self.assertEqual(lru_cache.get(3), 3)
        self.assertEqual(lru_cache.get(4), 4)


if __name__ == '__main__':
    unittest.main()
