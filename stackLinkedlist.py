from exceptions import Empty

class StackLL():
    class _Node():
        __slots__ = '_next', '_element'
    
        def __init__(self, e, next):
            self._next = next
            self._element = e
    
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise Empty('stack is empty')
        val = self._head._element
        self._head = self._head._next
        self._size -= 1
        return val

    def top(self):
        if self.isEmpty():
            raise Empty('stack is empty')
        return self._head._element

    def display(self):
        temp = self._head

        while temp:
            print(temp._element, end='-->')
            temp = temp._next
        print()

s = StackLL()

s.push(10)
s.display()

s.push(20)
s.push(30)
s.display()

print('pop', s.pop())
s.display()