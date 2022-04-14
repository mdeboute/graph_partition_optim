from structures import *
import copy, random
from utils import *


"""
Notion of neighborhoods:
    - We have a starting situation
    - You can take an element and put it elsewhere (Pick'n'Drop)
    - You can either take two elements and exchange them (Swap)
    - You can do a circular permutation (Sweep)
For this project we will use the Swap neighborhood.
"""

# swapEvaluator(solution, solutionCost, s) evaluate the new solution resulting of the swap 's' in solution 'solution'
# swap(solution, s) return the solution resulting of the swap 's' on solution 'solution'
# nSwap(solution, n) return 'n' random neighbor solutions of solution 'solution' (to upgrade)
# swapNeighborhood(solution) return all the neighbor solutions of solution 'solution'
# swapNodes(solution) return all the neighbor swaps of solution 'solution'


def swapEvaluator(solution, solutionCost, s):

    node1 = s[0]
    node1Class = s[1]
    node2 = s[2]
    node2Class = s[3]

    graph = solution.getGraph()
    partition = solution.getPartition()
    cost = solutionCost

    for n in partition[node1Class]:
        if n != node1:
            w1 = graph.getEdges()[node1][n]
            w2 = graph.getEdges()[node2][n]
            if w1 != 0:
                cost = cost + w1
            if w2 != 0:
                cost = cost - w2

    for n in partition[node2Class]:
        if n != node2:
            w1 = graph.getEdges()[node1][n]
            w2 = graph.getEdges()[node2][n]
            if w1 != 0:
                cost = cost - w1
            if w2 != 0:
                cost = cost + w2

    return cost


def nSwap(solution, n=20):
    k = solution.getNbClasses()
    swaps = []
    partition = solution.getPartition()

    while len(swaps) < n:
        switch = 0
        c1 = random.randint(0, k - 1)
        c2 = random.randint(0, k - 1)
        while c2 == c1:
            c2 = random.randint(0, k - 1)
        i = random.randint(0, len(partition[c1]) - 1)
        j = random.randint(0, len(partition[c2]) - 1)
        for s in swaps:
            if (s[0] == i or s[0] == j) and (s[1] == i or s[1] == j):
                switch = 121
        if switch == 0:
            tmp = [partition[c1][i], c1, partition[c2][j], c2]
            swaps.append(tmp)

    return swaps


def swapNeighborhood(solution):
    k = solution.getNbClasses()
    partitions = []
    partition = solution.getPartition()

    for c in range(k):
        for c2 in range(k):
            if c < c2:
                for node in partition[c]:
                    for node2 in partition[c2]:
                        tmp = copyPartition(partition)

                        tmp[c].remove(node)
                        tmp[c].append(node2)

                        tmp[c2].remove(node2)
                        tmp[c2].append(node)

                        partitions.append(Solution(tmp, solution.getGraph(), k))
    return partitions


def swap(solution, s):
    node1 = s[0]
    class1 = s[1]
    node2 = s[2]
    class2 = s[3]

    partition = solution.getPartition()

    partition[class1].remove(node1)
    partition[class1].append(node2)

    partition[class2].append(node1)
    partition[class2].remove(node2)

    solution = Solution(partition, solution.getGraph(), solution.getNbClasses())

    return solution


def swapNodes(solution):
    # return tab of swaps with the format [node1,class1,node2,class2]
    k = solution.getNbClasses()
    swaps = []
    partition = solution.getPartition()

    for c1 in range(k):
        for c2 in range(k):
            if c1 < c2:
                for node1 in partition[c1]:
                    for node2 in partition[c2]:
                        tmp = []
                        tmp.append(node1)
                        tmp.append(c1)
                        tmp.append(node2)
                        tmp.append(c2)
                        swaps.append(tmp)
    return swaps


def bestSwapNodesVoisinage(solution, solutionCost):
    swaps = swapNodes(solution)
    bestScore = solutionCost
    bestSol = solution

    for s in swaps:
        sCost = swapEvaluator(solution, solutionCost, s)
        if sCost < bestScore:
            tmp = copySolution(solution)
            bestSol = swap(tmp, s)
            bestScore = sCost
    return bestSol, bestScore