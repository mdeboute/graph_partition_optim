import time
from enumeration import basicEnum
from gradient_descent import *
from utils import *
from enum import *
from neighborhood import *
from metaheuristics import *

k = 2

t = time.time()
graph = parse("./data/centSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print(verbose=False)

partition = makeKPartition(graph, nbClasses=k)
solution = Solution(partition, graph, nbClasses=k)
t = time.time()
solutionCost = solution.getCost()
print(time.time() - t, "sec of getCost()")

# solution.print()

nNeighborhood = nSwap(solution, n=100)  # for metaheuristics & big instances
nodesNeighborhood = swapNodes(solution)


# Test for the nSwap method
############################
# print(neighborhood)
# print(nNeighborhood)
# print(nodesNeighborhood)
#############################


# Test for the enumeration
##########################
# print(basicEnum(graph, 30, nbClasses=k, verbose=True))
##########################
# 27 sec for the enumeration of the graph with 20 vertices and 2 classes is quite good


# Test for the gradientDescent
##############################
# print("Init sol at cost: ", solutionCost)
# t = time.time()
# bestSol, bestCost = gradientDescent(solution, solutionCost)
# print(
#     f"Best Gradient solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, time: ",
#     time.time() - t,
#     "sec",
# )
##############################

# Test for the betterGradientDescent
##############################
# print("Init sol at cost: ", solutionCost)
# t = time.time()
# bestSol, bestCost = betterGradientDescent(solution, solutionCost)
# print(
#     f"Best Gradient solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, time: ",
#     time.time() - t,
#     "sec",
# )
##############################


# Test for the simulatedAnnealing
#################################
# print("Init sol at cost: ", solutionCost)
# t = time.time()
# bestSol, bestCost = simulatedAnnealing(
#     solution,
#     solutionCost,
#     neighborhood=nodesNeighborhood,
#     maxIterations=graph.getNbVertices() * 10,
#     timeOut=3,
#     nswap=False,
#     neighborhoodSize=None,
#     initialTemperature=36,
#     finalTemperature=0.01,
#     coolingRate=0.09,
# )
# print(
#     f"Best solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, in time: {time.time() - t} sec",
# )
#################################


# Test for the tabuSearch
########################
# print("Init sol at cost: ", solutionCost)
# t = time.time()
# bestSol, bestCost = tabuSearch(
#     solution,
#     solutionCost,
#     iterMax=graph.getNbVertices() * 10,
#     timeOut=4,
# )
# print(
#     f"Best Tabou solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, time: ",
#     time.time() - t,
#     "sec",
# )
########################


# TODO: create executables and shell scripts for the different tests and make the report
