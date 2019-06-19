from exceptions import Empty

class Dequeue():
    def __init__(self):
        self._data = []
        self._front=0
        self._size=0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0
    
    def addFirst(self, data):
        self._data.insert(0, data)
        self._size +=1

    def addLast(self, data):
        self._data.append(data)
        self._size += 1
    
    def deleteFirst(self):
        if self.isEmpty():
            raise Empty('queue is empty')
        self._size -= 1
        return self._data.pop(0)

    def deleteLast(self):
        if self.isEmpty():
            raise Empty('queue is empty')
        self._size -= 1
        return self._data.pop()

    def first(self):
        if self.isEmpty():
            raise Empty('queue is empty')
        return self._data[self._front]

    def last(self):
        if self.isEmpty():
            raise Empty('queue is empty')
        return self._data[self._size-1]

q = Dequeue()
q.addFirst(10)
q.addFirst(20)
q.addFirst(30)
q.addLast(40)
print(q._data)

q.deleteFirst()
print(q._data)

q.deleteLast()
print(q._data)

