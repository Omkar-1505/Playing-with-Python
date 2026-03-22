class Graph:
    def __init__(self):
        self.adjlist = {} #dynamic

    def add_vertex(self,vertex):
        if vertex not in self.adjlist:
            self.adjlist[vertex] = [] #keys associated with empty lists

    def addEdge(self,src,dest):
        self.add_vertex(src) 
        self.add_vertex(dest) #if it is undirected graph
        self.adjlist[src].append(dest)
        self.adjlist[dest].append(src) #undirected graph

    def printGraph(self):
        for vertex in self.adjlist:
            print(vertex," -> ",self.adjlist[vertex], end="\n")

g = Graph()
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(1,4)
g.addEdge(4,3)
g.addEdge(2,4)
g.addEdge(4,5)
g.addEdge(3,5)
g.addEdge(5,6   )
g.printGraph()