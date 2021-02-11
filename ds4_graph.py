class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

    def edges(self):
        return self.findedges()

    # Find the distinct list of edges
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

    # Add the vertex as a key
    def addVertex(self, vrtx):
       if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    # Add the new edge
    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]


if __name__ == "__main__":

    # Create the dictionary with graph elements
    graph = { "a" : ["b","c"],
              "b" : ["a", "d"],
              "c" : ["a", "d"],
              "d" : ["e"],
              "e" : ["d"]
             }

    # Print the graph
    print(graph)
    # {'c': ['a', 'd'], 'a': ['b', 'c'], 'e': ['d'], 'd': ['e'], 'b': ['a', 'd']}

    g = Graph(graph)

    print(g.getVertices())
    # ['d', 'b', 'e', 'c', 'a']

    print(g.edges())
    # [{'b', 'a'}, {'b', 'd'}, {'e', 'd'}, {'a', 'c'}, {'c', 'd'}]

    g.addVertex("f")
    print(g.getVertices())
    # ['f', 'e', 'b', 'a', 'c','d']

    g.AddEdge({'a','e'})
    g.AddEdge({'a','c'})
    print(g.edges())
    # [{'e', 'd'}, {'b', 'a'}, {'b', 'd'}, {'a', 'c'}, {'a', 'e'}, {'c', 'd'}]