from Structures import *


def parser(file_path):
    """
    Parses the file and returns a Graph.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
        nb_vertices = int(lines[1].split()[0])
        nb_edges = int(lines[1].split()[1])
        dmin = int(lines[3].split()[0])
        dmax = int(lines[3].split()[1])
        edgesInfo = []
        degrees = []
        for i in range(5, 5 + nb_edges):
            edgesInfo.append(list(map(int, lines[i].split())))
        for i in range(6 + nb_edges, 6 + nb_edges + nb_vertices):
            degrees.append(int(lines[i].split()[1]))
    edges = []
    for info in edgesInfo:
        edges.append(Edge(info[0], info[1], info[2]))
    return Graph(nb_vertices, nb_edges, dmin, dmax, edges, degrees)