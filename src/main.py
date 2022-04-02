import time
from gradient_descent import gradientDescent
from utils import *
from enum import *
from random_partition import *
from neighborhood import *
from metaheuristics import simulatedAnnealing

t = time.time()
graph = parse("./data/trenteSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print(verbose=False)

partition = makeKPartition(graph, k=2)
solution = Solution(partition, graph)
neighborhood = swap(solution)

# print(gradientDescent(solution, neighborhood))

print(
    simulatedAnnealing(
        solution,
        neighborhood,
        initialTemperature=80,
        finalTemperature=0.01,
        coolingRate=0.08,
    )
)