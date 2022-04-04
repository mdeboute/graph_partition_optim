import time
from gradient_descent import gradientDescent
from utils import *
from enum import *
from random_partition import *
from neighborhood import *
from metaheuristics import simulatedAnnealing

t = time.time()
graph = parse("./data/cinquanteSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print(verbose=False)

partition = makeKPartition(graph, nbClasses=5)
solution = Solution(partition, graph, nbClasses=5)
neighborhood = swap(solution)

# print(gradientDescent(solution, neighborhood))

bestSol, bestCost = simulatedAnnealing(
    solution,
    neighborhood,
    initialTemperature=80,
    finalTemperature=0.01,
    coolingRate=0.08,
)

print(
    f"Best solution: {bestSol}, with cost: {bestCost}, feasible: {bestSol.isFeasible()}"
)

# 2 sec for 500 edges and 5 class is quite good I think?
