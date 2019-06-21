from exceptions import Empty

class QueueLL():

    class _Node():
        __slots__ = '_element', '_next'
        def __init__(self, e, next):
            self._element = e
            self._next = next
    
    def __init__(self):
        self._size = 0
        self._front = None
        self._rear = None

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, e):
        newNode = self._Node(e, None)

        if self.isEmpty():
            self._front = newNode
            self._rear = newNode
        else:
            self._rear._next = newNode
            self._rear = newNode
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Empty('Queue is empty')
        val = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isEmpty():
            self._rear = None
        return val

    def display(self):
        t = self._front

        while t:
            print(t._element, end='-->')
            t = t._next
        print()

    def first(self):
        if self.isEmpty():
            raise Empty('Queue is empty')

        return self._front._element

q = QueueLL()

q.enqueue(10)
q.enqueue(20)
q.display()

print('de', q.dequeue())

q.display()

print('front', q.first())