import math, random


def simulatedAnnealing(
    sol, neighborhood, initialTemperature, finalTemperature, coolingRate
):
    """
    Returns the best solution using the swap for the neighborhood.
    @param sol: the solution
    @param neighborhood: the neighborhood of the solution
    @param initialTemperature: the initial temperature
    @param finalTemperature: the final temperature
    @param coolingRate: the cooling rate
    @return: the best solution for the graph associated to the solution
    """
    bestSol = sol
    bestScore = sol.getCost()
    currTemperature = initialTemperature
    while currTemperature > finalTemperature:
        s = random.choice(neighborhood)
        delta = sol.getCost() - s.getCost()
        # we should normalize the delta because he have a huge impact on the metropolis criterion?
        if delta > 0 or random.uniform(0, 1) < math.exp(-delta / currTemperature):
            bestSol = s
        currTemperature *= coolingRate
    return bestSol, bestScore
