import time
from enumeration import basicEnum
from gradient_descent import *
from utils import *
from enum import *
from random_partition import *
from neighborhood import *
from metaheuristics import simulatedAnnealing

# nbClasses = 3

t = time.time()
graph = parse("./data/quatreSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print(verbose=True)

# partition = makeKPartition(graph, nbClasses)
# solution = Solution(partition, graph, nbClasses)

# neighborhood = swapNeighborhood(solution)
# nodesNeighborhood = swapNodes(solution)

# Test for the nSwap method
############################
# print(neighborhood)
# print(nSwap(solution, 2))
############################


# Test for the enumeration
##########################
# print(basicEnum(graph, verbose=False, nbClasses=2))
##########################
# 45 sec for the enumeration of the graph with 20 vertices and 2 classes


# Test for the gradientDescent
#############################
# print("Init sol at cost: ", solution.getCost())
# t = time.time()
# bestSol, bestCost = gradientDescent(solution, neighborhood)
# print(
#     f"\nBest solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, in: ", time.time()-t, "s"
# )
#############################

# Test for the partialGradientDescent
#####################################
# t = time.time()
# bestSol, bestCost = partialGradientDescent(
#     solution, solution.getCost(), nodesNeighborhood
# )
# print(
#     f"\nBest solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, in: ",
#     time.time() - t,
#     "s",
# )
#####################################


# Test for the simulatedAnnealing
#################################
# bestSol, bestCost = simulatedAnnealing(
#     solution,
#     neighborhood,
#     initialTemperature=80,
#     finalTemperature=0.01,
#     coolingRate=0.08,
# )
# print(
#     f"\nBest solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}"
# )
#################################
# 0.17 sec for 500 edges and 5 class is quite good I think?
