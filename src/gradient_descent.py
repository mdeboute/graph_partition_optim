from neighborhood import *
from random_partition import *


def gradientDescent(graph, k=2):
    """
    Returns the best solution using the swap for the neighborhood.
    @param graph: the graph
    @param k: the number of classes
    @return: the best solution of the graph
    """
    bestSolution = Solution(makeRandomPartition(graph, k), graph, k)
    bestNeighborhood = Neighborhood(bestSolution, graph)
    while bestNeighborhood.hasNext():
        solution = bestNeighborhood.next()
        if solution.getFitness() < bestSolution.getFitness():
            bestSolution = solution
            bestNeighborhood = Neighborhood(bestSolution, graph)
    return bestSolution
