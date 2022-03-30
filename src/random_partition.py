from Structures import *
import random


def makeBiPartition(nbVertices):
    """
    create a partition of the vertices into two classes
    the vertices are from 1 to N
    @param nbVertices: number of vertices
    @return: a bi-partition of the vertices
    """
    l = range(1, nbVertices + 1)  # the list of vertices
    k_1 = random.sample(l, int(nbVertices / 2))  # the first class
    k_2 = [x for x in l if x not in k_1]  # the second class
    k_1.sort()  # we sort the list
    return k_1, k_2


def makeKPartition(nbVertices, k=2):
    """
    create a partition of the vertices into k classes
    the vertices are from 1 to N
    @param nbVertices: number of vertices
    @return: a bi-partition of the vertices
    """
    l = []  # the list of vertices
    for i in range(nbVertices):
        l.append(i)

    partition = []
    counter = 0
    for c in range(k):
        partition.append([])
        for i in range(int((nbVertices / k) - ((nbVertices / k) % 1))):
            counter += 1
            j = random.sample(l, 1)
            partition[c].append(j[0])
            l.remove(j[0])
    for i in range(nbVertices - counter):
        j = random.sample(l, 1)
        partition[i].append(j[0])
        l.remove(j[0])
    return partition