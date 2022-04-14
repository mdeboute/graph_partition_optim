from neighborhood import *
import copy
from utils import copyPartition


def gradientDescent(sol, solCost, neighborhood):
    """
    Returns the best solution using the swap for the neighborhood.
    @param sol: the solution
    @param solCost: the cost of the solution
    @param neighborhood: the neighborhood of the solution
    @return: the best solution for the graph associated to the solution and the cost
    """
    bestSol = sol
    bestScore = solCost
    switch = 0

    for s in neighborhood:
        sCost = swapEvaluator(sol, solCost, s)
        if sCost < bestScore :
            # tmp = copy.deepcopy(sol)
            tmp = Solution(copyPartition(sol.getPartition()),sol.getGraph(),sol.getNbClasses())
            bestSol = swap(tmp,s)
            bestScore = sCost
            switch = 42
    if switch != 0:
        neighborhood = swapNodes(bestSol)
        return gradientDescent(bestSol, bestScore, neighborhood)
    else:
        return bestSol, bestScore
