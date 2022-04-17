import math, random, sys, time
from statistics import mean
from neighborhood import *
from utils import *


def simulatedAnnealing(
    solution,
    solutionCost,
    neighborhood,
    maxIterations,
    timeOut,
    nswap=False,
    neighborhoodSize=None,
    initialTemperature=36,
    finalTemperature=0.01,
    coolingRate=0.09,
):
    """
    Returns the best solution using the swap for the neighborhood.
    @param solution: the solution
    @param solutionCost: the cost of the solution
    @param neighborhood: the neighborhood
    @param maxIterations: the maximum number of iterations for the inner loop
    @param timeOut: the time out
    @param nswap: if True, the neighborhood is created with nSwap, otherwise with swapNodes
    @param neighborhoodSize: the size of the neighborhood (if nswap is True)
    @param initialTemperature: the initial temperature
    @param finalTemperature: the final temperature
    @param coolingRate: the cooling rate
    @return: the best solution and its cost
    """

    bestSol = solution
    bestCost = solutionCost
    currTemperature = initialTemperature
    i = 0
    nbhd = neighborhood
    t = time.time() + timeOut
    while currTemperature > finalTemperature:
        currSol = bestSol
        currCost = bestCost
        while i < maxIterations:
            if time.time() > t:
                print("Timeout reached!")
                return bestSol, bestCost
            s = random.choice(nbhd)
            sCost = swapEvaluator(currSol, currCost, s)
            delta = sCost - bestCost
            # normalize the delta because he have a huge impact on the metropolis criterion
            # to avoid overflow
            if delta < 0 or random.uniform(0, 1) <= math.exp(-delta / currTemperature):
                tmp = copySolution(currSol)
                bestSol = swap(tmp, s)
                bestCost = sCost
            i += 1
        if nswap == True:
            nbhd = nSwap(bestSol, neighborhoodSize)
        else:
            nbhd = swapNodes(bestSol)
        currTemperature *= coolingRate
        i = 0
    return bestSol, bestCost


def getInitialTemperature(
    solution,
    solutionCost,
    tau=0.8,
    k=100,
    neighborhoodSize=1000,
):
    """
    Returns the initial temperature for the simulated annealing.
    @param solution: the solution
    @param solutionCost: the cost of the solution
    @param tau: the acceptance rate
    @param k: the number of iterations
    @param neighborhoodSize: the size of the neighborhood
    @return: the initial temperature
    """

    neighborhood = nSwap(solution, neighborhoodSize)
    deltas = list()
    for _ in range(k):
        s1 = random.choice(neighborhood)
        s2 = random.choice(neighborhood)
        s1Cost = swapEvaluator(solution, solutionCost, s1)
        s2Cost = swapEvaluator(solution, solutionCost, s2)
        deltas.append(abs(s1Cost - s2Cost))
    meanDelta = mean(deltas)
    return -meanDelta / math.log(tau)


def tabouUpdate(tabu, x):
    """
    Updates the tabu list.
    @param tabu: the tabu list
    @param x: the solution
    @return: the updated tabu list
    """

    tabuSize = len(tabu)
    for i in range(tabuSize - 1):
        tabu[i] = tabu[i + 1]
    tabu[tabuSize - 1] = x
    return tabu


# arbitrary first choices :
# liberation if f(move) < f'(move) (with f' the cost of the solution when he was placed in tabu)
# it means you accept a move only if he is strictly better than he were the last time
# this is definitively up to discution and will probably be changed

# tabu take a solution and return the best solution he could find browsing the neighborhood solutions recursively
def tabuSearch(
    solution,
    solutionCost,
    iterMax,
    timeOut,
    tabuSize=7,
    nswap=True,
    neighborhoodSize=100,
    isAspirating=False,
):
    """
    Returns the best solution using the tabu search.
    @param solution: the solution
    @param solutionCost: the cost of the solution
    @param iterMax: the maximum number of iterations
    @param timeOut: the time out
    @param tabuSize: the size of the tabu list (default: 7)
    @param nswap: if True, the neighborhood is created with nSwap, otherwise with swapNodes (default: True)
    @param neighborhoodSize: the size of the neighborhood (if nswap is True, default: 100)
    @param isAspirating: if True, the tabu search is aspirating or not (default: False)
    @return: the best solution and its cost
    """

    if tabuSize <= 0:
        print("TabuSize must be > 0!")

    bestSol = solution
    bestCost = solutionCost
    actualIter = 0

    currentSol = bestSol
    currentScore = bestCost
    # why do we need currents you ask ? glad you did
    # we have optimals found that are put in bestSol and bestCost but we want to explore, sometimes we won't exit the program
    # at optimal found so we need some current solutions that are our iterations and best solutions for exit

    tabu = [None] * tabuSize

    t = time.time() + timeOut

    while actualIter < iterMax:
        if time.time() > t:
            print("Time out reached!")
            break
        actualIter += 1
        if nswap == True:
            neighborhood = nSwap(currentSol, neighborhoodSize)
        else:
            neighborhood = swapNodes(currentSol)

        currentBestSwap = []
        currentbestCost = sys.maxsize
        # surely we don't need a second set of current ! what are you doing step-lucas ? well glad you asked that too
        # in fact you may quite have not seen it in the GD but i did add a second set of solutions, "sol" was what currentSol is
        # and then i added a bestSol to keep in mind the best sol found so far, with keeping in memory sol (or currentSol)
        # to compute the cost of other swaps.
        # so that is why, surely, I need a 3rd set of solution/cost

        for s in neighborhood:
            if time.time() > t:
                print("Time out reached!")
                break
            sCost = swapEvaluator(currentSol, currentScore, s)
            isIntabu = 0
            for i in range(tabuSize):
                if tabu[i] is not None:
                    # print(s," and ",tabu[i])
                    if (s[0] == tabu[i][0] or s[0] == tabu[i][1]) and (
                        s[2] == tabu[i][0] or s[2] == tabu[i][1]
                    ):
                        isIntabu = i

            if isIntabu == 0:
                if sCost < currentbestCost:
                    currentbestCost = sCost
                    currentBestSwap = s
            else:
                if (sCost < tabu[isIntabu][2]) and (isAspirating != False):
                    tabu[isIntabu] = None
                    if sCost < currentbestCost:
                        currentbestCost = sCost
                        currentBestSwap = s
        # this is the big part of the algo so if you don't understand something, ask

        # we update tabu
        tabu = tabouUpdate(tabu, [s[0], s[2], currentbestCost])

        # we iterate in the best solution found
        # print(currentSol," to swap ",s)
        tmp = copySolution(currentSol)
        currentSol = swap(tmp, currentBestSwap)
        currentScore = currentbestCost

        if currentScore < bestCost:
            bestCost = currentScore
            bestSol = currentSol

    return bestSol, bestCost
