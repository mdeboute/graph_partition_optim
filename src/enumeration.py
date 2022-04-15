import time
from structures import *
import itertools, math


def basicEnum(graph, TimeOut, nbClasses=2, verbose=False):
    """
    A basic enumeration algorithm to find the better partition of the graph.
    @param graph: the graph
    @param TimeOut: the time limit
    @param nbClasses: the number of classes
    @param verbose: if True, prints the best solution
    @return: the best solution and its cost
    """
    t = time.time() + TimeOut
    bestCost = math.inf
    bestSol = None

    nbVertices = graph.getNbVertices()
    vertices = range(nbVertices)

    # we create the sets of possible classes for each vertex
    support = (range(nbClasses) for _ in vertices)

    # we create the iterator
    iter = itertools.product(*support)

    # for each answer of the iterator we create the partitions
    nbSol = 0  # nb of partitions found
    for rep in iter:
        if time.time() > t:
            print("Time out reached!")
            break
        sol = [[] for _ in range(nbClasses)]
        nbSol += 1

        # we transform an answer of the type (0,1,0,1) into [ [0,2], [1,3], [] ]
        for s, x in enumerate(rep):
            sol[x].append(s)  # vertex s is in partition number x

        solution = Solution(sol, graph, nbClasses)

        if solution.isFeasible():
            ev = solution.getCost()
            if ev < bestCost:
                bestCost = ev
                bestSol = solution

        if verbose:
            print("Sol = {0!r:23} numero = {1:02}".format(sol, nbSol))

    if nbSol != nbClasses ** nbVertices:
        print("The number of solutions found is not correct!")
    return bestSol, bestCost
