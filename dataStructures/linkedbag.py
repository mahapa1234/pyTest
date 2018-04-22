#encoding: utf-8
from node import Node

class LinkedBag(object):

    def __init__(self, sourceCollection = None):
        self._items = None
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)           #执行add方法

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def clear(self):
        self._size = 0
        self._items = Array()

    def add(self, item):
        self._items = Node(item, self._items)
        self._size += 1

    def __iter__(self):
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return "{" + ", ".join(map(str,self)) + "}"     #如无_iter_方法此打印失败

    def __add__(self, other):
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        if self is other: return True
        if type(self) != type(other) or \
            len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True

    def remove(self, item):
        if not item in self:
            raise KeyError(str(item) + "not in bag")
        probe = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        if probe == self._items:
            self._items = self._items.next
        else:
            trailer.next = probe.next
        self._size -= 1

if __name__ == '__main__':
    a = LinkedBag([3,4,5,6,7,8])
    print a
    a.remove(5)
    print a