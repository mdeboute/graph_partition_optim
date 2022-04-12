import math, random, sys
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


# arbitrary first choices :
# liberation if f(move) < f'(move) (with f' the cost of the solution when he was placed in tabou)
# it means you accept a move only if he is strictly better than he were the last time
# this is definitively up to discution and will probably be changed

# tabou take a solution and return the best solution he could find browsing the neighborhood solutions recursively
def tabou(solution,tabouSize,itermax) :
    
    if (tabouSize<=0) : 
        print("\n\n /!\ invalid tabou size /!\ \n\n")
    
    bestSol = solution
    bestScore = solution.getCost()
    actualIter = 0
    
    currentSol = bestSol
    currentScore = bestScore
    # why do we need currents you ask ? glad you did
    # we have optimals found that are put in bestSol and bestScore but we want to explore, sometimes we won't exit the program
    # at optimal found so we need some current solutions that are our iterations and best solutions for exit
    
    tabou = [None]*tabouSize
    
    while (actualIter<itermax) :
        actualIter+=1
        neighborhood = swapNodes(currentSol)
        currentBestSwap = []
        currentBestScore = sys.maxsize
        # surely we don't need a second set of current ! wtf are you doing lucas ? well glad you asked that too
        # in fact you may quite have not seen it in the GD but i did add a second set of solutions, "sol" was what currentSol is
        # and then i added a bestSol to keep in mind the best sol found so far, with keeping in memory sol (or currentSol)
        # to compute the cost of other swaps. 
        # so that is why, surely, I need a 3rd set of solution/cost
        
        for s in neighborhood :
            sCost = swapEvaluator(currentSol,currentScore,s)
            isInTabou = 0
            for i in range(tabouSize) :
                if tabou[i] is not None :
                    #print(s," and ",tabou[i])
                    if (s[0]==tabou[i][0] or s[0]==tabou[i][1]) and (s[2]==tabou[i][0] or s[2]==tabou[i][1]) :
                        isInTabou = i
            
            if (isInTabou==0) :
                if sCost < currentBestScore :
                    currentBestScore = sCost
                    currentBestSwap = s
            else :
                if sCost < tabou[isInTabou][2] :
                    tabou[isInTabou] = None
                    if sCost < currentBestScore :
                        currentBestScore = sCost
                        currentBestSwap = s
        #this is the big part of the algo so if you don't understand something, ask
        
        
        # we update tabou
        for i in range (tabouSize-1) :
            tabou[i] = tabou[i+1]
        tabou[tabouSize-1] = [s[0],s[2],currentBestScore]
        
        # we iterate in the best solution found
        #print(currentSol," to swap ",s)
        tmp = copy.deepcopy(currentSol)
        currentSol = swap(tmp,currentBestSwap)
        currentScore = currentBestScore
        
        if currentScore < bestScore :
            bestScore = currentScore
            bestSol = currentSol
        
    return bestSol, bestScore
