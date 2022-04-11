import time
from enumeration import basicEnum
from gradient_descent import *
from utils import *
from enum import *
from random_partition import *
from neighborhood import *
from metaheuristics import simulatedAnnealing

k = 2

t = time.time()
graph = parse("./data/centSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print(verbose=False)

partition = makeKPartition(graph, nbClasses=k)
solution = Solution(partition, graph, nbClasses=k)

# nNeighborhood = nSwap(solution, 5) # for metaheuristics/big instances
nodesNeighborhood = swapNodes(solution)
neighborhood = swapNeighborhood(solution)


# Test for the nSwap method
############################
# print(neighborhood)
# print(nSwap(solution, 2))
############################


# Test for the enumeration
##########################
# print(basicEnum(graph, verbose=False, nbClasses=k))
##########################
# 27 sec for the enumeration of the graph with 20 vertices and 2 classes is quite good


# Test for the gradientDescent
#############################
# print("Init sol at cost: ", solution.getCost())
# t = time.time()
# bestSol, bestCost = gradientDescent(solution, neighborhood)
# print(
#     f"\nBest solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, time: ",
#     time.time() - t,
#     "sec",
# )
#############################

# Test for the partialGradientDescent
#####################################
# t = time.time()
# bestSol, bestCost = partialGradientDescent(
#     solution, solution.getCost(), nodesNeighborhood
# )
# print(
#     f"Best solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, time: ",
#     time.time() - t,
#     "sec",
# )
#####################################


# Test for the simulatedAnnealing
#################################
# bestSol = simulatedAnnealing(
#     solution,
#     neighborhood=neighborhood,
#     initialTemperature=30,
#     finalTemperature=0.01,
#     coolingRate=0.1,
#     maxIterations=10,
#     sizeNeighborhood=5,
# )
# print(
#     f"Best solution: {bestSol}, with cost: {bestSol.getCost()}, feasible: {bestSol.isFeasible()}"
# )
#################################