
class BinaryTree():
    class Node():
        def __init__(self, e):
            self.e = e
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def addNode(self, e, node):
        if self.isEmpty():
            self.root = self.Node(e)
        else:
            if node.e > e:
                if node.left == None:
                    node.left = self.Node(e)
                else:
                    self.addNode(e, node.left)
            elif node.e < e:
                if node.right == None:
                    node.right = self.Node(e)
                else:
                    self.addNode(e, node.right)


    def display(self, node):
        if node:
            print(node.e, end='--')
            self.display(node.left)
            
            self.display(node.right)


b = BinaryTree()

b.addNode(30, b.root)
b.addNode(20, b.root)
b.addNode(10, b.root)
b.addNode(50, b.root)
b.addNode(60, b.root)

b.display(b.root)