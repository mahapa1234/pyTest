#encoding: utf-8

class Array(object):
    """ Represents an array. """
    def __init__(self, capacity, fillValue = None):
        """
         capacity is the static size of the array.
         fillValue is placed at each position.
        """
        self._items = list()
        for count in range(capacity):
            self._items.append(fillValue)

    def __len__(self):
        """the capacity of the array."""
        return len(self._items)

    def __str__(self):
        """the string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """supports traversal with a for loop."""
        return iter(self._items)

    def __getitem__(self, index):
        """subscripts operator for access at index."""
        return self._items[index]

    def __setitem__(self, index, newItem):
        """subscripts operator for replacement at index."""
        self._items[index] = newItem

if __name__ == '__main__':
    a = Array(5)
    print len(a)
    print a
    for i in xrange(len(a)):
        a[i] = i+1
    print str(a), a[2]
