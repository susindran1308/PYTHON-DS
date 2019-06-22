from queueLinkedlist import QueueLL
class BinaryTree():

    class _Node():
        __slots__ = '_element', '_left', '_right'

        def __init__(self, e, left=None, right=None):
            self._element = e
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None
        self._size = 0

    def maketree(self, e, left, right):
        self._root = self._Node(e, left._root, right._root)
        left._root = None
        right._root = None

    def levelorder(self):
        q = QueueLL()
        t = self._root
        print(t._element, end='-->')
        q.enqueue(t)

        while not q.isEmpty():
            t = q.dequeue()
            if t._left:
                print(t._left._element, end='-->')
                q.enqueue(t._left)
            if t._right:
                print(t._right._element, end='-->')
                q.enqueue(t._right)
        print()

    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end='-->')
            self.inorder(troot._right)

    def preorder(self, troot):
        if troot:
            print(troot._element, end='-->')
            self.inorder(troot._left)
            self.inorder(troot._right)

    def postorder(self, troot):
        if troot:
            self.inorder(troot._left)
            self.inorder(troot._right)
            print(troot._element, end='-->')

x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
a = BinaryTree()

x.maketree(40, a, a)
y.maketree(60, a, a)
z.maketree(20,x, a)
r.maketree(50, a, y)
s.maketree(30, r, a)
t.maketree(10, z, s)

t.levelorder()

t.preorder(t._root)
print()

t.postorder(t._root)
print()

t.inorder(t._root)
print()