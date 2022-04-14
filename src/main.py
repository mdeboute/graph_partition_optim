import time
from enumeration import basicEnum
from gradient_descent import *
from utils import *
from enum import *
from random_partition import *
from neighborhood import *
from metaheuristics import simulatedAnnealing

k = 3

t = time.time()

graph = parse("./data/cinqCentSommets.txt")

print(time.time() - t, "seconds of parsing")

graph.print(verbose=False)

partition = makeKPartition(graph, k)
solution = Solution(partition, graph, k)
neighborhood = swapNeighborhood(solution)
nodesNeighborhood = swapNodes(solution)

# preuve du cancer !
# p2 = partition
# s2 = Solution(p2,graph,k)
# print(partition)
# swap(s2,[p2[0][0],0,p2[1][0],1])
# print(partition)

# solved cancer
# p2 = []
# for i in range(len(partition)) :
#     tmp = []
#     for j in range(len(partition[i])) :
#         tmp.append(partition[i][j])
#     p2.append(tmp)

# print("partition : ", partition)
# print("p2 : ",p2)
# s2 = Solution(p2,graph,k)
# swap(s2,[p2[0][0],0,p2[1][0],1])
# print("new partition : ",partition)
# print("new p2 : ",p2)

#test solved cancer
# p2 = copyPartition(partition)
# s2 = Solution(p2,graph,k)
# print(p2)
# print("here : ",partition)
# swap(s2,[p2[0][0],0,p2[1][0],1])
# print("there : ",partition)
# youhou copyPartition works !!!!

#test perf deepcopy vs mycopy
# t = time.time()
# tmp = copy.deepcopy(partition)
# dt = time.time()-t
# t = time.time()
# tmp = copyPartition(partition)
# mt = (time.time()-t)
# print(dt/mt," of factor gain")
# factor 6 on 500nodes

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

print("init sol at cost of : ",solution.getCost())

# classical gradientDescent
#############################

# t = time.time()
# bestSol, bestCost = gradientDescent(solution, neighborhood)

# print(
#     f"\nBest solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}, in : ", time.time()-t, "s"
# )

# partial gradientDescent
#############################

# t = time.time()
# bestSolP, bestCostP = partialGradientDescent(solution, solution.getCost(),nodesNeighborhood)

# print(
#     f"\nBest solution: {bestSolP}, with cost: {bestCostP}, feasible: {bestSolP.isFeasible()}, in : ", time.time()-t, "s"
# )

#############################
# 0.4 sec for 30 vertices and 2 classes


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

# Test for the Tabou
#################################
# bestSol, bestCost = Tabou(
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