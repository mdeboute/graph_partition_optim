from Structures import *
import copy
from evaluateur import *


"""
Notion of neighborhoods:
    - We have a starting situation
    - You can take an element and put it elsewhere (Pick'n'Drop)
    - You can either take two elements and exchange them (Swap)
    - You can do a circular permutation (Sweep)

Naming convention :
    - XXX_one: returns one item
    - delta_XXX: returns the elementary movement
    - XXX_name_YYY: name is the neighborhood name
    - XXX_gen: returns an iterator
"""

def swapVoisinage (soluce) :
    k = soluce.getNbClasses()
    partitions = []
    partition = soluce.getPartition()

    for c in range(k):
        for c2 in range(k):
            if c < c2:
                print(c," ",c2)
                for node in partition[c]:
                    for node2 in partition[c2]:
                        tmp = copy.deepcopy(partition)
                        tmp[c].remove(node)
                        tmp[c].append(node2)

                        tmp[c2].remove(node2)
                        tmp[c2].append(node)

                        print(tmp)

                        partitions.append(partition)
    return partitions
#ne rend pas des partitions triee. probleme ?

def pickNDropVoisinage (soluce,classToDrop) :
    k = soluce.getNbClasses()
    try :
        if (k<classToDrop) :
            raise Exception("trying to drop from not existing class")
    except Exception as e :
        print(e)
    partitions = []
    partition = soluce.getPartition()
    for node in partition[classToDrop]:
        for c in range(k) :
            if (c!=classToDrop) :
                tmp = copy.deepcopy(partition)
                tmp[c].append(node)
                tmp[classToDrop].remove(node)

                print(tmp)

                partitions.append(tmp)
    return partitions

def bestSwapVoisinage (soluce) :
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

                        tmpSol = Solution(tmp,soluce.getGraph(),soluce.getNbClasses())
                        ev = evaluateur(tmpSol)
                        if (opt==-1) :
                            opt = ev
                            bestPartition = tmp
                        if (ev<opt) :
                            opt = ev
                            bestPartition = tmp
    return bestPartition

def bestPickNDropVoisinage (soluce,classToDrop) :
    k = soluce.getNbClasses()
    try :
        if (k<classToDrop) :
            raise Exception("trying to drop from not existing class")
    except Exception as e :
        print(e)
    
    opt = -1
    bestPartition = []

    partition = soluce.getPartition()

    for node in partition[classToDrop]:
        for c in range(k) :
            if (c!=classToDrop) :
                tmp = copy.deepcopy(partition)
                tmp[c].append(node)
                tmp[classToDrop].remove(node)

                tmpSol = Solution(tmp,soluce.getGraph(),soluce.getNbClasses())
                ev = evaluateur(tmpSol)
                if (ev<opt) :
                    opt = ev
                    bestPartition = tmp
    return bestPartition



