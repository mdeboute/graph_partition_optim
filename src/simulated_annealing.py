import math, random


def simulatedAnnealing(
    sol, neighborhood, initialTemperature, coolingRate, finalTemperature
):
    """
    Returns the best solution using the swap for the neighborhood.
    @param sol: the solution
    @param initialTemperature: the initial temperature
    @param neighborhood: the neighborhood
    @param coolingRate: the cooling rate
    @param finalTemperature: the final temperature
    @param maxIterations: the maximum number of iterations
    @return: the best solution of the graph
    """
    bestScore = sol.getCost()
    bestSol = sol
    temperature = initialTemperature
    while temperature > finalTemperature:
        s = random.choice(neighborhood)
        delta = s.getCost() - sol.getCost()
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            sol = s
            if s.getCost() < bestScore:
                bestScore = s.getCost()
                bestSol = s
        temperature *= coolingRate
    return bestSol, bestScore