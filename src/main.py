import time
from gradient_descent import gradientDescent
from utils import *
from enum import *
from random_partition import *
from neighborhood import *
from simulated_annealing import simulatedAnnealing

t = time.time()
graph = parser("./data/vingtSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print(verbose=False)

partition = makeKPartition(graph, k=3)
solution = Solution(partition, graph, nbClasses=3)
neighborhood = swap(solution)

print(gradientDescent(solution, neighborhood))

# print(
#     simulatedAnnealing(
#         solution,
#         neighborhood,
#         initialTemperature=100,
#         coolingRate=0.09,
#         finalTemperature=0.01,
#     )
# )


# TODO: fix the gradient descent method