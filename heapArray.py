from exceptions import Empty

class HeapArray():
    def __init__(self):
        self.maxsize = 10
        self.data = [-1]*self.maxsize
        self.currentsize = 0

    def __len__(self):
        return self.currentsize

    def isEmpty(self):
        return self.currentsize == 0

    def maxh(self):
        if self.isEmpty():
            raise Empty('Heap is empty')
        else:
            return self.data[1] #heap starts from index 1

    def insert(self, e):
        if self.currentsize == self.maxsize:
            raise Empty('No space')
        self.currentsize +=1
        i = self.currentsize

        while i!=1 and e > self.data[i//2]:
            self.data[i] = self.data[i//2]
            i = i//2
        self.data[i] = e

    def deletemax(self):
        x = self.data[1] # root is always deleted
        y = self.data[currentsize] # assigning last element to root
        self.currentsize-1

        i=1
        ci=2
        #bubblng up operations
        while ci <= self.currentsize:
            if ci < self.currentsize and self.data[ci] < self.data[ci+1]: #checking the greater child for swapping
                ci += 1
            if y >= self.data[ci]:
                break
            self.data[i] = self.data[ci]
            i=ci
            ci = ci*2
        self.data[i] = y

h = HeapArray()

h.insert(10)
h.insert(40)
h.insert(30)
h.insert(20)
h.insert(60)
print(h.data)
h.insert(50)
print(h.data)