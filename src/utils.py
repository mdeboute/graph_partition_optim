from Structures import *


def parser(file_path):
    """
    Parses the file and returns a Graph.
    """
    with open(file_path, "r") as f:
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


# only thing to check is "nearly equal", with a tab of assignment we already make it so we assign one and only one class each
# also, overloading to check solution cost in the same time
def checker(solution):
    nbClasses = solution.nbClasses
    partition = solution.partition
    Tab = [0] * nbClasses
    for i in partition:
        if i < 0 or i >= nbClasses:
            print("solution given give an assignment of " + i)
            return 0
        Tab[i] += 1
    for i in range(1, nbClasses):
        if Tab[i] > Tab[0] + 1 or Tab[i] < Tab[0] + 1:
            print("assignment not nearly equal")
            return 0
    return 1


def checker(solution, graph):
    nbClasses = solution.nbClasses
    partition = solution.partition
    Tab = [0] * nbClasses
    for i in partition:
        if i < 0 or i >= nbClasses:
            print("solution given give an assignment of " + i)
            return -1
        Tab[i] += 1
    for i in range(1, nbClasses):
        if Tab[i] > Tab[0] + 1 or Tab[i] < Tab[0] + 1:
            print("assignment not nearly equal")
            return -2
    if evaluater(solution, graph) == solution.getCost():
        return solution.getCost()
    print("cost diff between solution and eval when checking")
    return -3


# it is very sad to browse the edges when you have 10^8 but meh, no other way if you want to check ponctually and here, m<n^2
def evaluater(solution, graph):
    s = 0
    for e in graph.edges:
        if solution.partition[e.source] != solution.partition[e.destination]:
            s += 1
    return s


# TODO: test the checker and evaluater methods
