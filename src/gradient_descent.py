from neighborhood import *
import copy

def gradientDescent(sol, neighborhood):
    """
    Returns the best solution using the swap for the neighborhood.
    @param sol: the solution
    @param neighborhood: the neighborhood of the solution
    @return: the best solution for the graph associated to the solution
    """
    bestSol = sol
    bestScore = sol.getCost()
    for s in neighborhood:
        if s.getCost() < bestScore:
            bestSol = s
            bestScore = s.getCost()
            # and we update the neighborhood of the new best solution
            neighborhood = swapNeighborhood(bestSol)
    if bestScore != sol.getCost():
        return gradientDescent(bestSol, neighborhood)
    else:
        return bestSol, bestScore

def partialGradientDescent(sol, solCost, neighborhood):
    """
    Returns the best solution using the swap for the neighborhood.
    @param sol: the solution
    @param neighborhood: the neighborhood of the solution
    @return: the best solution for the graph associated to the solution
    """
    bestSol = sol
    bestScore = solCost
    switch = 0
    
    for s in neighborhood:
        sCost = swapEvaluator(sol, solCost, s)
        if sCost < bestScore :
            tmp = copy.deepcopy(sol)
            bestSol = swap(tmp,s)
            bestScore = sCost
            switch = 42
    if switch != 0 :
        neighborhood = swapNodes(bestSol)
        return partialGradientDescent(bestSol,bestScore, neighborhood)
    else:
        return bestSol, bestScore
