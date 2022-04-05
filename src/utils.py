from structures import *


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

        degrees = []
        for i in range(6 + nbEdges, 6 + nbEdges + nbVertices):
            degrees.append(int(lines[i].split()[1]))

        return Graph(nbVertices, nbEdges, edges, degrees)
