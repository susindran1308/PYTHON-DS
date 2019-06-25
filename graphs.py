# import numpy as np

class Graph():

    def __init__(self, vertices):
        self.vertices = vertices
        self.adjmat = [[0 for _ in range(vertices)] for __ in range(vertices)]
        self.edges = 0

    def insertEdge(self, u, v, w=1):
        self.adjmat[u][v] = w
        self.edges += 1


    def deleteEdge(self, u, v):
        self.adjmat[u][v] = 0
        self.edges -= 1

    def getEdge(self, u, v):
        return self.adjmat[u][v]

    def verticesCount(self):
        return self.vertices

    def edgeCount(self):
        return self.edges

    def indegree(self, u):
        count=0
        for i in range(self.vertices):
            if not self.adjmat[i][u] == 0:
                count+=1

        return count

    def outdegree(self, u):
        count=0
        for i in range(self.vertices):
            if not self.adjmat[i][u] == 0:
                count+=1

        return count

    def display(self):
        for row in self.adjmat:
            print(*row)

g = Graph(7)
g.display()
print('\n')
g.insertEdge(0,1)
g.insertEdge(0,5)
g.insertEdge(0,6)
g.insertEdge(1,2)
g.insertEdge(1,5)
g.insertEdge(1,6)
g.insertEdge(2,3)
g.insertEdge(2,4)
g.insertEdge(2,6)
g.insertEdge(3,4)
g.insertEdge(4,2)
g.insertEdge(4,5)
g.insertEdge(5,2)
g.insertEdge(5,3)
g.insertEdge(6,3)

g.display()

print('Vertices:', g.verticesCount())
print('Edges:', g.edgeCount())

print('outdegree of 2:', g.outdegree(2))
print('indegree of 6:', g.indegree(6))