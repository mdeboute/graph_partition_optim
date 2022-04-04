from neighborhood import *
from random_partition import *

# def DescenteDeGradiant (soluce) :
#     k = soluce.getNbClasses
#     champion = soluce.getPartition()
#     championPower = evaluateur(soluce)

#     isHavingFun = 1 # yay !

#     challenger = []

#     challengerPower = -1

#     while (isHavingFun == 1) :
#         isHavingFun = 0 # ho...

#         challenger = bestSwapVoisinage(soluce) # a new challenger arise
#         equippedChallenger = Solution(challenger,soluce.getGraph(),soluce.getNbClasses())
#         challengerPower = evaluateur(equippedChallenger)

#         if (challengerPower < championPower) :
#             print("descente")
#             isHavingFun = 1 # bloodbath yay
#             champion = challenger # new champion is crown
#             championPower = challengerPower

#     return champion


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
    if bestScore != sol.getCost():
        return gradientDescent(bestSol, neighborhood)
    else:
        return bestSol, bestScore
