import time
from enumeration import basicEnum
from gradient_descent import *
from utils import *
from enum import *
from random_partition import *
from neighborhood import *
from metaheuristics import *

k = 2

t = time.time()
graph = parse("./data/centSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print(verbose=False)

partition = makeKPartition(graph, nbClasses=k)
solution = Solution(partition, graph, nbClasses=k)

nNeighborhood = nSwap(solution, 10)  # for metaheuristics/big instances
nodesNeighborhood = swapNodes(solution)
neighborhood = swapNeighborhood(solution)


# Test for the swap's methods
#############################
# print(neighborhood)
# print(nSwap(solution, 2))
# print(nodesNeighborhood)
#############################


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
t = time.time()
bestSol, bestCost = partialGradientDescent(
    solution, solution.getCost(), nodesNeighborhood
)
print(
    f"Best solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, time: ",
    time.time() - t,
    "sec",
)
#####################################


# Test for the simulatedAnnealing
#################################
# print("Init sol at cost: ", solution.getCost())

# bestSol, bestCost = simulatedAnnealing(
#     solution,
#     neighborhood=nNeighborhood,
#     initialTemperature=22,
#     finalTemperature=0.01,
#     coolingRate=0.095,
#     maxIterations=10,
#     sizeNeighborhood=10,
# )
# print(
#     f"Best solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}"
# )
#################################

# Test for the tabou
#####################################
print("Init sol at cost: ", solution.getCost())
t = time.time()
bestSol, bestCost = tabou(solution,7,graph.nbVertices)
print(
    f"Best solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, time: ",
    time.time() - t,
    "sec",
)

#################################

# TODO: create executables and shell scripts for the different tests and make the report
