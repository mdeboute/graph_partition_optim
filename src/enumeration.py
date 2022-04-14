from structures import *
import itertools
import math


def basicEnum(graph, verbose=False, nbClasses=2):
    """
    Returns the best solution.
    @param graph: the graph
    @print: the best solution for the graph associated to the solution and the cost
    """
    opt = math.inf
    bestSol = None

    vertices = range(1, graph.getNbVertices() + 1)

    # we create the sets of possible classes for each vertex
    support = (range(nbClasses) for _ in vertices)

    # we create the iterator
    iter = itertools.product(*support)

    # for each answer of the iterator we create the partitions
    nbSol = 0  # nb of partitions found
    for rep in iter:
        sol = [[] for _ in range(nbClasses)]
        nbSol += 1

        # we transform an answer of the type (0,1,0,1) into [ [0,2], [1,3], [] ]
        for s, x in enumerate(rep):
            sol[x].append(s)  # vertex s is in partition number x

        solution = Solution(sol, graph, nbClasses)

        if solution.isFeasible():
            ev = solution.getCost()
            if ev < opt:
                opt = ev
                bestSol = solution

        if verbose:
            print("Sol = {0!r:23} numero = {1:02}".format(sol, nbSol))

    # We check that we have had the right number of answers
    _msg = "Found: {found:d} partitions. "
    _msg += "Expected: {expected:d} > "
    _msg += "diagnostic {status}"
    d = {"found": nbSol, "expected": nbClasses ** graph.getNbVertices()}
    d["status"] = d["found"] == d["expected"]
    print(_msg.format(**d))
    print(f"\nBest solution: {bestSol}, with cost: {opt}")
