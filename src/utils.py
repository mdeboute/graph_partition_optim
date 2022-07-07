from structures import *
import random


def parse(file_path):
    """
    Parses the file and returns a Graph.
    @param file_path: the path to the file
    @return: a graph
    """

    # surround the file with try/except
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()

            nbVertices = int(lines[1].split()[0])
            nbEdges = int(lines[1].split()[1])

            # save the edges information as an adjacency matrix
            # where the value (i, j) is the weight of the edge (i, j)
            # or 0 if there is no edge
            edges = [[0 for _ in range(nbVertices)] for _ in range(nbVertices)]
            for i in range(5, 5 + nbEdges):
                # vertices are from 1 to nbVertices, so we need to substract 1
                src = int(lines[i].split()[0]) - 1
                dest = int(lines[i].split()[1]) - 1
                weight = int(lines[i].split()[2])
                edges[src][dest] = weight
                edges[dest][src] = weight

            degrees = []
            for i in range(6 + nbEdges, 6 + nbEdges + nbVertices):
                degrees.append(int(lines[i].split()[1]))

            return Graph(nbVertices, nbEdges, edges, degrees)
    except FileNotFoundError:
        print("File not found!")
        exit(1)


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
    """
    Copy a partition.
    @param partition: a partition
    @return: a copy of the partition
    """

    copy = []
    for i in range(len(partition)):
        tmp = []
        for j in range(len(partition[i])):
            tmp.append(partition[i][j])
        copy.append(tmp)
    return copy


def copySolution(solution):
    """
    Copy a solution.
    @param solution: a solution
    @return: a copy of the solution
    """

    return Solution(
        copyPartition(solution.getPartition()),
        solution.getGraph(),
        solution.getNbClasses(),
    )
