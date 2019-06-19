from exceptions import Empty
class Stack():
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0
    
    def push(self, data):
        self._data.append(data)

    def pop(self):
        if self.isEmpty():
            raise Empty("Stack is Empty")
        return self._data.pop()

    def top(self):
        if self.isEmpty():
            raise Empty("Stack is Empty")
        return self._data[-1]

    def display(self):
        print(*self._data)

stack = Stack()
stack.push(10)
stack.push(20)
stack.display()
print(len(stack))
print(stack.pop())
stack.display()
print(stack.pop())
print(len(stack))