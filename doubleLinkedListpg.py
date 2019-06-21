from exceptions import Empty

class DOubleLL():
    class _Node():
        __slots__ = '_element', '_prev', '_next'
        def __init__(self, e, next, prev):
            self._element = e
            self._next = next
            self._prev = prev

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def addFirst(self, e):
        newNode = self._Node(e, None, None)

        if self.isEmpty():
            self._head = newNode
            self._tail = newNode

        else:
            newNode._next = self._head
            self._head._prev = newNode
            self._head = newNode
        self._size += 1

    def addLast(self, e):
        newNode = self._Node(e, None, None)
        if self.isEmpty():
            self._head = newNode
            self._tail = newNode

        else:
            newNode._prev = self._tail
            self._tail._next = newNode
            self._tail = newNode
        self._size += 1

    def addAny(self, e, pos):
        newNode = self._Node(e, None, None)
        i=1
        thead = self._head

        while i < pos:
            thead = thead._next
            i += 1
        newNode._next = thead._next
        newNode._next._prev = newNode
        newNode._prev = thead
        thead._next = newNode
        self._size += 1

    def removeFirst(self):
        if self.isEmpty():
            raise Empty('list is empty')

        else:
            value = self._head._element
            self._head = self._head._next
            self._head._prev = None
            self._size -= 1
            if self.isEmpty():
                self._tail = None
            return value

    def removeLast(self):
        if self.isEmpty():
            raise Empty('list is empty')
        else:
            value = self._tail._element
            self._tail = self._tail._prev
            self._tail._next = None
            self._size -= 1
            if self.isEmpty():
                self._head = None
            return value

    def removeAny(self, pos):
        if self.isEmpty():
            raise Empty('list is empty')

        else:
            thead = self._head
            i=1
            while i< pos:
                thead = thead._next
                i += 1
            value = thead._next._element
            thead._next = thead._next._next
            thead._next._next._prev = thead
            self._size -= 1
            return value

    def display(self):
        thead = self._head
        while(thead):
            print(thead._element, end="-->")
            thead = thead._next
        print()

l = DOubleLL()
l.addLast(10)
l.addLast(20)
l.addLast(30)
l.display()

l.addFirst(40)
l.addFirst(50)
l.display()

l.addAny(20,2)
l.addAny(30,4)
l.display()

l.removeFirst()
l.display()

l.removeLast()
l.display()

l.removeAny(2)
l.display()
