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
graph = parse("./data/trenteSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print(verbose=False)

partition = makeKPartition(graph, nbClasses=k)
solution = Solution(partition, graph, nbClasses=k)

neighborhood = swapNeighborhood(solution)
nodesNeighborhood = swapNodes(solution)

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
# bestSol, bestCost = simulatedAnnealing(
#     solution,
#     neighborhood,
#     initialTemperature=80,
#     finalTemperature=0.01,
#     coolingRate=0.08,
# )
# print(
#     f"Best solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}"
# )
#################################
# 0.17 sec for 500 edges and 5 class is quite good I think?
