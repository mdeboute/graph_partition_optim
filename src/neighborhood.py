from Structures import *
import copy

"""
Notion of neighborhoods:
    - We have a starting situation
    - You can take an element and put it elsewhere (Pick'n'Drop)
    - You can either take two elements and exchange them (Swap)
    - You can do a circular permutation (Sweep)
"""


def swapVoisinage(solution):
    k = solution.nbClasses
    partitions = []
    partition = solution.getPartition()

    print("root :", partition)

    for c in range(k):
        for c2 in range(k):
            if c < c2:
                print(c, " ", c2)
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


# ne rend pas des partitions triee. probleme ?


def pickNDropVoisinage(solution, classToDrop):
    k = solution.nbClasses
    try:
        if k < classToDrop:
            raise Exception("trying to drop from not existing class")
    except Exception as e:
        print(e)
    partitions = []
    partition = solution.getPartition()
    print("root :", partition)
    for node in partition[classToDrop]:
        for c in range(k):
            if c != classToDrop:
                tmp = copy.deepcopy(partition)
                tmp[c].append(node)
                tmp[classToDrop].remove(node)

                print(tmp)

                partitions.append(tmp)
    return partitions


# should be functionnal, just need a functionnal getCost

# def bestSwapVoisinage (solution,classToDrop) :
#     k = solution.nbClasses
#     partition = solution.getPartition()

#     opt = -1
#     bestPartition = []

#     print ("root :", partition)

#     for c in range(k):
#         for c2 in range(k):
#             if c < c2:
#                 for node in partition[c]:
#                     for node2 in partition[c2]:
#                         tmp = copy.deepcopy(partition)
#                         tmp[c].remove(node)
#                         tmp[c].append(node2)

#                         tmp[c2].remove(node2)
#                         tmp[c2].append(node)

#                         ev = getCost(tmp)
#                         if (ev<opt) :
#                             opt = ev
#                             bestPartition = tmp
#     return bestPartition

# def bestPickNDropVoisinage (solution,classToDrop) :
#     k = solution.nbClasses
#     try :
#         if (k<classToDrop) :
#             raise Exception("trying to drop from not existing class")
#     except Exception as e :
#         print(e)

#     opt = -1
#     bestPartition = []

#     partition = solution.getPartition()

#     print ("root :", partition)
#     for node in partition[classToDrop]:
#         for c in range(k) :
#             if (c!=classToDrop) :
#                 tmp = copy.deepcopy(partition)
#                 tmp[c].append(node)
#                 tmp[classToDrop].remove(node)

#                 ev = getCost(tmp)
#                 if (ev<opt) :
#                     opt = ev
#                     bestPartition = tmp
#     return bestPartition
