#Depth First Search
#when lost in a puzzle/maze
#minimum spanning tree(avoid cycling)
#backtracing in stack
class Graph:
    def __init__(self,vertex):
        self.mat = [[0]*vertex for x in range(vertex)]
        self.size = vertex

    def add_edge(self,src,dest):
        if (0<=src<self.size and 0<=dest< self.size):
            self.mat[src][dest]=1 #for weight we have to put the weight in place of 1
            self.mat[dest][src] = 1 #only for undirected graph
        else:
            print("Invalid Edge")

    def print(self):
        for row in self.mat:
            print(' '.join(map(str,row)))

    def dfs(self,src):
        visited = [False]*self.size
        stack = [src]
        while(stack):
            v= stack.pop()   #last vertex
            if (visited[v] == False): 
                print(v,end=" -> ")
                visited[v]=True
            for i in range(self.size):
                if self.mat[v][i]==1 and visited[i]==False:  #stack vertex checking
                    stack.append(i) #stack refilling

g = Graph(6)
g.add_edge(0,1)   
g.add_edge(0,2)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(3,5)
g.add_edge(4,5)
g.dfs(0)     



#also possible using recursion