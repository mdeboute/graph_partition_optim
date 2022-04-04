from Structures import *
import copy
import random

"""
Notion of neighborhoods:
    - We have a starting situation
    - You can take an element and put it elsewhere (Pick'n'Drop)
    - You can either take two elements and exchange them (Swap)
    - You can do a circular permutation (Sweep)
"""


def swap(solution):
    k = solution.getNbClasses()
    partitions = []
    partition = solution.getPartition()

    for c in range(k):
        for c2 in range(k):
            if c < c2:
                for node in partition[c]:
                    for node2 in partition[c2]:
                        tmp = copy.deepcopy(partition)

                        tmp[c].remove(node)
                        tmp[c].append(node2)

                        tmp[c2].remove(node2)
                        tmp[c2].append(node)

                        partitions.append(Solution(tmp, solution.getGraph(), k))
    return partitions


def pickNDropVoisinage(soluce, classToDrop):
    k = soluce.getNbClasses()
    try:
        if k < classToDrop:
            raise Exception("trying to drop from not existing class")
    except Exception as e:
        print(e)
    partitions = []
    partition = soluce.getPartition()
    for node in partition[classToDrop]:
        for c in range(k):
            if c != classToDrop:
                tmp = copy.deepcopy(partition)
                tmp[c].append(node)
                tmp[classToDrop].remove(node)

                print(tmp)

                partitions.append(tmp)
    return partitions


def bestSwapVoisinage(soluce):
    k = soluce.getNbClasses()
    partition = soluce.getPartition()

    opt = -1
    bestPartition = []

    for c in range(k):
        for c2 in range(k):
            if c < c2:
                for node in partition[c]:
                    for node2 in partition[c2]:
                        tmp = copy.deepcopy(partition)
                        tmp[c].remove(node)
                        tmp[c].append(node2)

                        tmp[c2].remove(node2)
                        tmp[c2].append(node)

                        tmpSol = Solution(tmp, soluce.getGraph(), soluce.getNbClasses())
                        ev = evaluateur(tmpSol)
                        if opt == -1:
                            opt = ev
                            bestPartition = tmp
                        if ev < opt:
                            opt = ev
                            bestPartition = tmp
    return bestPartition


def bestPickNDropVoisinage(soluce, classToDrop):
    k = soluce.getNbClasses()
    try:
        if k < classToDrop:
            raise Exception("trying to drop from not existing class")
    except Exception as e:
        print(e)

    opt = -1
    bestPartition = []

    partition = soluce.getPartition()

    for node in partition[classToDrop]:
        for c in range(k):
            if c != classToDrop:
                tmp = copy.deepcopy(partition)
                tmp[c].append(node)
                tmp[classToDrop].remove(node)

                tmpSol = Solution(tmp, soluce.getGraph(), soluce.getNbClasses())
                ev = evaluateur(tmpSol)
                if ev < opt:
                    opt = ev
                    bestPartition = tmp
    return bestPartition


def nSwap(solution, n):
    # this method allows us to obtain a neighborhood of size n
    k = solution.getNbClasses()
    partition = solution.getPartition()
    partitions = []

    for c in range(k):
        for c2 in range(k):
            if c < c2:
                p = list(partition[c:n])
                # random.shuffle(p)
                p2 = list(partition[c2:n])
                # random.shuffle(p2)
                for node in p:
                    for node2 in p2:
                        tmp = copy.deepcopy(partition)

                        if tmp[c].count(node) == 1:
                            tmp[c].remove(node)
                            tmp[c].append(node2)

                        if tmp[c2].count(node2) == 1:
                            tmp[c2].remove(node2)
                            tmp[c2].append(node)

                        partitions.append(Solution(tmp, solution.getGraph(), k))

    return partitions


# def pickNDrop(solution, classToDrop):
#     k = solution.getNbClasses()
#     try:
#         if k < classToDrop:
#             raise Exception("trying to drop from not existing class")
#     except Exception as e:
#         print(e)
#     partitions = []
#     partition = solution.getPartition()
#     print("root :", partition)
#     for node in partition[classToDrop]:
#         for c in range(k):
#             if c != classToDrop:
#                 tmp = copy.deepcopy(partition)
#                 tmp[c].append(node)
#                 tmp[classToDrop].remove(node)

#                 print(tmp)

#                 partitions.append(tmp)
#     return partitions

# TODO: test the pickNDrop method and create a nSwap method that will return a list of n neighbors for huge graphs
