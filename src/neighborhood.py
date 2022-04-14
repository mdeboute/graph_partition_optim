from structures import *
import copy, random


"""
Notion of neighborhoods:
    - We have a starting situation
    - You can take an element and put it elsewhere (Pick'n'Drop)
    - You can either take two elements and exchange them (Swap)
    - You can do a circular permutation (Sweep)
"""

# swapEvaluator(solution, solutionCost, s) evaluate the new solution resulting of the swap 's' in solution 'solution'
# swap(solution,s) return the solution resulting of the swap 's' on solution 'solution'
# nSwap(solution,n) return 'n' random neighbor solutions of solution 'solution' (to upgrade)
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
            if graph.getEdges()[node1][n] != 0 :
                cost = cost + 1
            if graph.getEdges()[node2][n] != 0 :
                cost = cost - 1

    for n in partition[node2Class]:
        if n != node2:
            if graph.getEdges()[node1][n] != 0 :
                cost = cost - 1
            if graph.getEdges()[node2][n] != 0 :
                cost = cost + 1

    return cost


def nSwap(solution, n):
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
    while switch == 0 and len(partitions) < n:
        tmp = copy.deepcopy(partition)

        nvalue1 = tmp[c1][node1]
        nvalue2 = tmp[c2][node2]
        
        tmp[c1].remove(nvalue1)
        tmp[c1].append(nvalue2)

        tmp[c2].remove(nvalue2)
        tmp[c2].append(nvalue1)

        partitions.append(Solution(tmp, graph, k))

        node2 = node2 + 1
        if node2 == len(partition[c2]):
            node2 = 0
            c2 = c2 + 1
            if c2 == len(partition):
                node1 = node1 + 1
                if node1 == len(partition[c1]):
                    node1 = 0
                    c1 = c1 + 1
                    if c1 == len(partition) - 1:
                        switch = 1
                c2 = c1 + 1

    return partitions


def swapNeighborhood(solution):
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

def swap (solution,s) :
    node1 = s[0]
    class1 = s[1]
    node2 = s[2]
    class2 = s[3]

    partition = solution.getPartition()

    partition[class1].remove(node1)
    partition[class1].append(node2)

    partition[class2].append(node1)
    partition[class2].remove(node2)

    solution = Solution(partition,solution.getGraph(),solution.getNbClasses())

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

# TODO: test the pickNDrop method and create (fix) the nSwap method
# that will return a random list of n neighbors (useful for huge graphs)
# + refactor the code with the new methods structure,
# btw i don't think that the new evaluators are needed anymore
