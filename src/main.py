import time
from enumeration import basicEnum
from gradient_descent import *
from utils import *
from enum import *
from neighborhood import *
from metaheuristics import *

k = 2

t = time.time()
graph = parse("./data/vingtSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print(verbose=False)

partition = makeKPartition(graph, nbClasses=k)
solution = Solution(partition, graph, nbClasses=k)
t = time.time()
solutionCost = solution.getCost()
print(time.time() - t, "sec of getCost()")

# solution.print()

nNeighborhood = nSwap(solution, n=100)  # for metaheuristics & big instances
# nodesNeighborhood = swapNodes(solution)
# neighborhood = swapNeighborhood(solution)


# Test for the nSwap method
############################
# print(neighborhood)
# print(nNeighborhood)
# print(nodesNeighborhood)
#############################


# Test for the enumeration
##########################
print(basicEnum(graph, 30, nbClasses=k, verbose=True))
##########################
# 27 sec for the enumeration of the graph with 20 vertices and 2 classes is quite good


# Test for the gradientDescent
##############################
# print("\nInit sol at cost: ", solutionCost)
# t = time.time()
# bestSol, bestCost = gradientDescent(solution, solutionCost)
# print(
#     f"\nBest Gradient solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, time: ",
#     time.time() - t,
#     "sec",
# )
# if (bestCost!=bestSol.getCost()) :
#     print ("\n/!\ alerte rouge /!\ \n")

# Test for the betterGradientDescent
##############################
# print("\nInit sol at cost: ", solutionCost)
# t = time.time()
# bestSol, bestCost = betterGradientDescent(solution, solutionCost)
# print(
#     f"\nBest betterGradient solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, time: ",
#     time.time() - t,
#     "sec",
# )
# if (bestCost!=bestSol.getCost()) :
#     print ("\n/!\ alerte rouge /!\ \n")
##############################


# Test for the simulatedAnnealing
#################################
# print("Init sol at cost: ", solutionCost)
# bestSol, bestCost = simulatedAnnealing(
#     solution,
#     solutionCost,
#     neighborhood=nNeighborhood,
#     maxIterations=graph.getNbVertices(),
#     nswap=True,
#     neighborhoodSize=100,
#     initialTemperature=230,
#     finalTemperature=0.01,
#     coolingRate=0.2,
# )
# print(
#     f"Best solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}"
# )
#################################


# Test for the tabuSearch
#########################
# print("Init sol at cost: ", solutionCost)
# t = time.time()
# bestSol, bestCost = tabuSearch(solution, 7, graph.getNbVertices() // 2)
# print(
#     f"Best Tabou solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, time: ",
#     time.time() - t,
#     "sec",
# )
########################

# Test for the tabuSearchNSwap
#########################
# print("Init sol at cost: ", solutionCost)
# t = time.time()
# bestSol, bestCost = tabuSearch(solution, solutionCost, 7, graph.getNbVertices()*100000, 1, 1, 900)
# print(
#     f"Best Tabou nSwap solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, time: ",
#     time.time() - t,
#     "sec",
# )
########################


# TODO: create executables and shell scripts for the different tests and make the report
