class Vertex:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.edges = None
        self.minDistance = None
        self.previousVertex = None



class Edge:
    def __init__(self, source: int, target: int, weight: int):
        self.source = source
        self.target = target
        self.weight = weight



class Dijkstra:
    def __init__(self):
        pass

    def computePath(self, sourceId):
        pass

    def getShortestPathTo(self, targetId):
        pass

    def createGraph(self, vertexes, edgesToVertexes):
        pass

    def resetDijkstra(self):
        pass

    def getVertexes(self):
        pass
