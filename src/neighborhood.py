from telnetlib import TM
from Structures import *
import copy


"""
Notion of neighborhoods:
    - We have a starting situation
    - You can take an element and put it elsewhere (Pick'n'Drop)
    - You can either take two elements and exchange them (Swap)
    - You can do a circular permutation (Sweep)
"""

def swapEvaluator(solution,solutionCost,node1,node1Class,node2,node2Class):
    graph = solution.getGraph()
    partition = solution.getPartition()
    cost = solutionCost
    
    for n in partition [node1Class] :
        if n !=  node1 :
            if graph.getEdge(node1, n) is not None :
                cost = cost+1
            if graph.getEdge(node2, n) is not None :
                cost= cost-1
        
    for n in partition [node2Class] :
        if n != node2 :
            if graph.getEdge(node1, n) is not None :
                cost = cost-1
            if graph.getEdge(node2, n) is not None :
                cost = cost+1
        
    return cost

def nSwap(solution,n):
    k = solution.getNbClasses()
    partitions = []
    partition = solution.getPartition()
    graph = solution.getGraph()

    random.shuffle(partition)
    for c in range(k):
        random.shuffle(partition[c])
    # partition fully shuffled at that point
    
    switch = 0
    
    c1 = 0
    c2 = 1
    node1 = 0
    node2 = 0
    while (switch==0 and len(partitions)<n ) :
        tmp = copy.deepcopy(partition)

        nvalue1 = tmp[c1][node1]
        nvalue2 = tmp[c2][node2]
        print(" swap ", nvalue1, " and ",nvalue2, " from ", c1, " and ", c2)
        tmp[c1].remove(nvalue1)
        tmp[c1].append(nvalue2)

        tmp[c2].remove(nvalue2)
        tmp[c2].append(nvalue1)

        partitions.append(Solution(tmp, graph, k))
        
        node2=node2+1
        if (node2==len(partition[c2])) :
            node2 = 0
            c2 = c2+1
            if (c2==len(partition)) :
                node1 = node1+1
                if (node1==len(partition[c1])) :
                    node1 = 0
                    c1 = c1+1
                    if (c1 == len(partition)-1) :
                        switch = 1
                c2 = c1+1
    
    return partitions

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
                        ev = tmpSol.getCost()
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
                ev = tmpSol.getCost()
                if ev < opt:
                    opt = ev
                    bestPartition = tmp
    return bestPartition


#def nSwap(solution, n):
#    # this method allows us to obtain a neighborhood of size n
#    k = solution.getNbClasses()
#    partition = solution.getPartition()
#    partitions = []
#
#    for c in range(k):
#        for c2 in range(k):
#            if c < c2:
#                p = list(partition[c:n])
#                # random.shuffle(p)
#                p2 = list(partition[c2:n])
#                # random.shuffle(p2)
#                for node in p:
#                    for node2 in p2:
#                        tmp = copy.deepcopy(partition)
#
#                        if tmp[c].count(node) == 1:
#                            tmp[c].remove(node)
#                            tmp[c].append(node2)
#
#                        if tmp[c2].count(node2) == 1:
#                            tmp[c2].remove(node2)
#                            tmp[c2].append(node)
#
#                        partitions.append(Solution(tmp, solution.getGraph(), k))
#
#    return partitions
# obsolete ?

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

# TODO: test the pickNDrop method and create (fix) the nSwap method
# that will return a random list of n neighbors
# (useful for huge graphs)
