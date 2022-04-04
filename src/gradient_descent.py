from neighborhood import *


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
            neighborhood = swap(bestSol)
    if bestScore != sol.getCost():
        return gradientDescent(bestSol, neighborhood)
    else:
        return bestSol, bestScore
