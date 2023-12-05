class Vertex:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.edges = []
        self.minDistance = float('inf')
        self.previousVertex = None


class Edge:
    def __init__(self, source: int, target: int, weight: int):
        self.source = source
        self.target = target
        self.weight = weight


class Dijkstra:
    def __init__(self):
        self.vertexes = []

    def computePath(self, sourceId):
        visited = []
        queue = []
        start = None

        for ver in self.vertexes:
            if ver.id == sourceId:
                start = ver
        start.minDistance = 0
        queue.append(start)

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)

                for edge in node.edges:
                    neighbour = None
                    for v in self.vertexes:
                        if v.id == edge.target:
                            neighbour = v
                    if neighbour not in visited:
                        if edge.weight + node.minDistance < neighbour.minDistance:
                            neighbour.minDistance = edge.weight + node.minDistance
                            neighbour.previousVertex = node

                        if neighbour in queue:
                            queue.remove(neighbour)

                        if len(queue) == 0:
                            queue.append(neighbour)
                        else:
                            for q in range(len(queue)):
                                if queue[q].minDistance > neighbour.minDistance:
                                    queue.insert(q, neighbour)
                                    break
                                elif q == len(queue) - 1:
                                    queue.append(neighbour)


    def getShortestPathTo(self, targetId):
        path = []
        node = None
        for i in self.vertexes:
            if i.id == targetId:
                node = i
        if node.minDistance != 0 and node.previousVertex is None:
            return []
        else:
            while node.minDistance != 0:
                path.append(node)
                node = node.previousVertex
            path.append(node)
            return path[::-1]


    def createGraph(self, vertexes, edgesToVertexes):
        for vertex in vertexes:
            for edge in edgesToVertexes:
                if vertex.id == edge.source:
                    vertex.edges.append(edge)
            self.vertexes.append(vertex)

    def resetDijkstra(self):
        for vert in self.vertexes:
            vert.minDistance = float('inf')
            vert.previousVertex = None

    def getVertexes(self):
        return self.vertexes
