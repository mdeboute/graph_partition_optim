from neighborhood import *
from random_partition import *


def gradientDescent(sol, neighborhood):
    """
    Returns the best solution using the swap for the neighborhood.
    @param graph: the graph
    @param k: the number of classes
    @return: the best solution of the graph
    """
    bestScore = sol.getCost()
    bestSol = sol
    for s in neighborhood:
        if s.getCost() < bestScore:
            bestScore = s.getCost()
            bestSol = s
    if bestScore != sol.getCost():
        return gradientDescent(bestSol, neighborhood)
    else:
        return bestSol, bestScore
