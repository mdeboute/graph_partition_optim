from neighborhood import *
import copy
from utils import *

# look at the whole neighborhood 
def gradientDescent(sol, solCost, nswaps=0):
    """
    Returns the best solution using the swap for the neighborhood.
    @param sol: the solution
    @param solCost: the cost of the solution
    @param neighborhood: the neighborhood of the solution
    @return: the best solution for the graph associated to the solution and the cost
    """
    bestS = []
    bestScore = solCost
    switch = 0

    if (nswaps==1):
        neighborhood = nSwap(sol,100)
    else :
        neighborhood = swapNodes(sol)

    for s in neighborhood:
        sCost = swapEvaluator(sol, solCost, s)
        if sCost < bestScore :
            bestS = s
            bestScore = sCost
            switch = 42
    if switch != 0:
        tmp = copySolution(sol)
        bestSol = swap(tmp,bestS)
        
        return gradientDescent(bestSol, bestScore)
    else:
        return sol, solCost


# take the 1st solution that better ou cost.
def betterGradientDescent(sol, solCost, nswaps=0):
    """
    Returns the best solution using the swap for the neighborhood.
    @param sol: the solution
    @param solCost: the cost of the solution
    @param neighborhood: the neighborhood of the solution
    @return: the best solution for the graph associated to the solution and the cost
    """
    if (nswaps==1):
        neighborhood = nSwap(sol,100)
    else :
        neighborhood = swapNodes(sol)

    for s in neighborhood:
        sCost = swapEvaluator(sol, solCost, s)
        if sCost < solCost :
            tmp = swap(sol,s)
            return betterGradientDescent(tmp, sCost)
    else:
        return sol, solCost
