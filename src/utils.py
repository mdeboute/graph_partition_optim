from structures import *
import random


def parse(file_path):
    """
    Parses the file and returns a Graph.
    """
    with open(file_path, "r") as f:
        lines = f.readlines()

        nbVertices = int(lines[1].split()[0])
        nbEdges = int(lines[1].split()[1])

        # save the edges information as an adjacency matrix
        # where the value (i, j) is the weight of the edge (i, j)
        # or 0 if there is no edge
        edges = [[0 for j in range(nbVertices)] for i in range(nbVertices)]
        for i in range(5, 5 + nbEdges):
            edges[int(lines[i].split()[0]) - 1][int(lines[i].split()[1]) - 1] = int(
                lines[i].split()[2]
            )
            edges[int(lines[i].split()[1]) - 1][int(lines[i].split()[0]) - 1] = int(
                lines[i].split()[2]
            )

        degrees = []
        for i in range(6 + nbEdges, 6 + nbEdges + nbVertices):
            degrees.append(int(lines[i].split()[1]))

        return Graph(nbVertices, nbEdges, edges, degrees)


def makeKPartition(graph, nbClasses=2):
    """
    Create a partition of the vertices into k classes,
    the vertices are from 0 to N-1.
    @param graph: a graph
    @return: a k-partition of the vertices
    """
    nbVertices = graph.getNbVertices()
    l = [_ for _ in range(nbVertices)]  # the list of vertices
    partition = list()
    counter = 0
    for c in range(nbClasses):
        partition.append([])
        for i in range(int((nbVertices / nbClasses) - ((nbVertices / nbClasses) % 1))):
            counter += 1
            j = random.sample(l, 1)
            partition[c].append(j[0])
            l.remove(j[0])
    for i in range(nbVertices - counter):
        j = random.sample(l, 1)
        partition[i].append(j[0])
        l.remove(j[0])
    return partition


def copyPartition(partition):
    copy = []
    for i in range(len(partition)):
        tmp = []
        for j in range(len(partition[i])):
            tmp.append(partition[i][j])
        copy.append(tmp)
    return copy


def copySolution(solution):
    return Solution(
        copyPartition(solution.getPartition()),
        solution.getGraph(),
        solution.getNbClasses(),
    )
