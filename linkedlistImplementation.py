from exceptions import Empty

class LinkedList():
    class _Node():
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def addFirst(self, e):
        newNode = self._Node(e, None)

        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
        else:
            newNode._next = self._head
            self._head = newNode
        self._size += 1

    def addLast(self, e):
        newNode = self._Node(e, None)

        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
        else:
            self._tail._next = newNode
            self._tail = newNode
        self._size += 1
    
    def addAny(self, e, pos):
        newNode = self._Node(e, None)

        thead = self._head
        i = 1
        while i < pos:
            thead = thead._next
            i += 1

        newNode._next = thead._next
        thead._next = newNode
        self._size += 1

    def removeFirst(self):
        if self.isEmpty():
            raise Empty('List is empty')

        value = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.isEmpty():
            self._tail = None
        return value

    def removeLast(self):
        if self.isEmpty():
            raise Empty('List is empty')

        thead = self._head
        i=1
        while i < len(self) - 1:
            thead = thead._next
            i += 1
        self._tail = thead
        value = thead._next._element
        self._tail._next = None
        self._size -= 1
        return value

    def removeAny(self, pos):
        if self.isEmpty():
            raise Empty('List is empty')

        i=1
        thead = self._head
        while i < pos-1:
            thead = thead._next
            i += 1
        value = thead._next._element
        thead._next = thead._next._next
        self._size -= 1
        return value
    
    def display(self):
        thead = self._head
        while thead:
            print(thead._element, end="-->")
            thead = thead._next
        print()

l = LinkedList()
l.addFirst(10)
l.addFirst(20)
l.addFirst(30)
l.display()

l.addLast(40)
l.addLast(50)
l.addLast(60)
l.display()

l.addAny(11, 2)
l.addAny(22, 5)
l.addAny(33, 4)
l.display()

l.removeAny(2)
l.removeFirst()
l.removeLast()
l.display()