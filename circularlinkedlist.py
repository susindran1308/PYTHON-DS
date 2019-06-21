from exceptions import Empty

class CircularLL():
    class _Node():
        __slots__ = '_element', '_next'

        def __init__(self, element, next=None):
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
        newNode = self._Node(e)

        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
            self._tail._next = self._head

        else:
            newNode._next = self._head
            self._tail._next = newNode
            self._head = newNode
        self._size += 1

    def addLast(self, e):
        newNode = self._Node(e)

        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
            self._tail._next = self._head
        
        else:
            self._tail._next = newNode
            self._tail = newNode
            self._tail._next = self._head
        self._size += 1

    def addAny(self, e, pos):
        newNode = self._Node(e)

        i=1
        thead = self._head
        while i  < pos:
            thead = thead._next
            i += 1
        newNode._next = thead._next
        thead._next = newNode
        self._size += 1


    def removeFirst(self):
        if self.isEmpty():
            raise Empty('List is empty')

        else:
            value = self._head._element
            self._head = self._head._next
            self._tail._next = self._head
            self._size -= 1
            if self.isEmpty():
                self._tail = None
            return value


    def removeLast(self):
        if self.isEmpty():
            raise Empty('List is empty')

        else:
            i =1
            thead = self._head
            while i < self._size -1:
                thead = thead._next
                i += 1
            value = self._tail._element
            thead._next = self._head._next
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
        i=0
        thead = self._head
        while i < self._size:
            print(thead._element,  end="-->")
            thead = thead._next
            i+=1
        print()

cll = CircularLL()

cll.addFirst(10)
cll.addLast(20)
cll.addAny(30,2)
cll.display()