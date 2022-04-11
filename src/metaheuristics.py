import math, random
from neighborhood import *


def simulatedAnnealing(
    sol,
    neighborhood,
    initialTemperature,
    finalTemperature,
    coolingRate,
    maxIterations,
    sizeNeighborhood,
):
    """
    Returns the best solution using the swap for the neighborhood.
    @param sol: the solution
    @param neighborhood: the neighborhood
    @param initialTemperature: the initial temperature
    @param finalTemperature: the final temperature
    @param coolingRate: the cooling rate
    @param maxIterations: the maximum number of iterations
    @param sizeNeighborhood: the size of the neighborhood
    @return: the best solution for the graph associated to the initial solution
    """
    bestSol = sol
    currTemperature = initialTemperature
    k = 0
    nbhd = neighborhood
    while currTemperature > finalTemperature:
        while k < maxIterations:
            k += 1
            s = random.choice(nbhd)
            delta = bestSol.getCost() - s.getCost()
            # normalize the delta because he have a huge impact on the metropolis criterion
            # to avoid overflow
            delta = delta / math.sqrt(sizeNeighborhood)
            if delta > 0 or random.uniform(0, 1) < math.exp(-delta / currTemperature):
                bestSol = s
                nbhd = nSwap(bestSol, sizeNeighborhood)
        currTemperature *= coolingRate
        k = 0
    return bestSol
