from neighborhood import *
from utils import *
import time


def gradientDescent(sol, solCost, timeout=60, nswap=False, neighborhoodSize=100):
    """
    Returns the best solution from looking at the whole neighborhood.
    @param sol: the solution
    @param solCost: the cost of the solution
    @param nswap: if True, use the nSwap neighborhood
    @param neighborhoodSize: the size of the neighborhood
    @return: the best solution and its cost
    """
    bestSol = sol
    bestCost = solCost
    switch = 0

    if nswap == True:
        neighborhood = nSwap(sol, neighborhoodSize)
    else:
        neighborhood = swapNodes(sol)

    for s in neighborhood:
        if (time.time() > timeout) :
            print("timeout reached!")
            switch = 0
            break
        sCost = swapEvaluator(sol, solCost, s)
        if sCost < bestCost:
            bestSol = s
            bestCost = sCost
            switch = 42
            
    
    if switch != 0:
        tmp = copySolution(sol)
        bestSol = swap(tmp, bestSol)

        return gradientDescent(bestSol, bestCost, timeout, nswap, neighborhoodSize)
    else:
        return sol, solCost


def betterGradientDescent(sol, solCost, timeout=60, nswap=False, neighborhoodSize=100):
    """
    Returns the best solution while looking at the first improving solution.
    @param sol: the solution
    @param solCost: the cost of the solution
    @param nswap: if True, use the nSwap neighborhood
    @param neighborhoodSize: the size of the neighborhood
    @return: the best solution and its cost
    """
    if nswap == True:
        neighborhood = nSwap(sol, neighborhoodSize)
    else:
        neighborhood = swapNodes(sol)

    for s in neighborhood:
        if (time.time() > timeout) :
            print("timeout reached!")
            switch = 0
            break
        sCost = swapEvaluator(sol, solCost, s)
        if sCost < solCost:
            tmp = swap(sol, s)
            return betterGradientDescent(tmp, sCost, timeout, nswap, neighborhoodSize)
    else:
        return sol, solCost