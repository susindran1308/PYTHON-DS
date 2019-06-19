from exceptions import Empty

class Queue():
    def __init__(self):
        self._data = []
        self._size=0
        self._front = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, data):
        self._data.append(data)
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Empty("Queue is empty.")
        else:
            x = self._data.pop(0)
            self._size -= 1
            return x

    def first(self):
        if self.isEmpty():
            raise Empty("Queue is empty.")
        return self._data[self._front]

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())
print(q.dequeue())
print(q.first())
print(len(q))
print(q.dequeue())
print(q.dequeue())

    