import random


def makeKPartition(graph, nbClasses=2):
    """
    create a partition of the vertices into k classes
    the vertices are from 1 to N
    @param graph: a graph
    @return: a k-partition of the vertices
    """
    l = []  # the list of vertices
    for i in range(graph.getNbVertices()):
        l.append(i)

    partition = []
    counter = 0
    for c in range(nbClasses):
        partition.append([])
        for i in range(
            int(
                (graph.getNbVertices() / nbClasses)
                - ((graph.getNbVertices() / nbClasses) % 1)
            )
        ):
            counter += 1
            j = random.sample(l, 1)
            partition[c].append(j[0])
            l.remove(j[0])
    for i in range(graph.getNbVertices() - counter):
        j = random.sample(l, 1)
        partition[i].append(j[0])
        l.remove(j[0])
    for _ in range(nbClasses):
        partition[_].sort()
    return partition
