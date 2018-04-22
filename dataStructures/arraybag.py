#encoding: utf-8

from arrays import Array

class ArrayBag(object):
    """An array-based bag implementation."""

    DEFAULT_CAPACITY = 10

    def __init__(self, sourceCollection = None):
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
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
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        self._items[len(self)] = item
        self._size += 1

    def __iter__(self):
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

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
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        for i in range(targetIndex,len(self)-1):
            self._items[i] = self._items[i+1]
        self._size -= 1

if __name__ == '__main__':
    a = ArrayBag([1,2,3,4,5])
    a.remove(1)
    print a
    # b = ArrayBag([1,2,3,4,5])
    # print a==b
    # print len(a)
    # a.add(3)
    # print len(a)
    # print a.clear()
    # print a.isEmpty()
    # for i in a:
    #     print i
    # print a
