from neighborhood import *
import copy
from utils import *


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
            tmp = copySolution(sol)
            bestSol = swap(tmp,s)
            bestScore = sCost
            switch = 42
    if switch != 0:
        neighborhood = swapNodes(bestSol)
        return gradientDescent(bestSol, bestScore, neighborhood)
    else:
        return bestSol, bestScore

def betterGradientDescent(sol, solCost, neighborhood):
    """
    Returns the best solution using the swap for the neighborhood.
    @param sol: the solution
    @param solCost: the cost of the solution
    @param neighborhood: the neighborhood of the solution
    @return: the best solution for the graph associated to the solution and the cost
    """
    for s in neighborhood:
        sCost = swapEvaluator(sol, solCost, s)
        if sCost < solCost :
            tmp = swap(sol,s)
            return gradientDescent(tmp, solCost, swapNodes(tmp))
    else:
        return sol, solCost
