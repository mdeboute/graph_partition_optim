import math, random
from statistics import mean
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
    bestCost = sol.getCost()
    currTemperature = initialTemperature
    i = 0
    nbhd = neighborhood
    while currTemperature > finalTemperature:
        while i < maxIterations:
            s = random.choice(nbhd)
            sCost = s.getCost()
            delta = sCost - bestCost
            # normalize the delta because he have a huge impact on the metropolis criterion
            # to avoid overflow
            if delta < 0:
                bestSol = s
                bestCost = sCost
            elif random.uniform(0, 1) <= math.exp(-delta / currTemperature):
                bestSol = s
            i += 1
        nbhd = nSwap(bestSol, sizeNeighborhood)
        currTemperature *= coolingRate
        i = 0
    return bestSol, bestCost


def getInitialTemperature(solution, tau=0.8, k=100, neighborhoodSize=100):
    neighborhood = nSwap(solution, neighborhoodSize)
    deltas = list()
    for _ in range(k):
        s1 = random.choice(neighborhood)
        s2 = random.choice(neighborhood)
        s1Cost = s1.getCost()
        s2Cost = s2.getCost()
        deltas.append(abs(s1Cost - s2Cost))
    meanDelta = mean(deltas)
    return -meanDelta / math.log(tau)


# TODO: implement the tabuSearch