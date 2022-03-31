import time
from gradient_descent import gradientDescent
from utils import *
from enum import *
from random_partition import *
from neighborhood import *

t = time.time()
graph = parser("./data/vingtSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print(verbose=False)

partition = makeBiPartition(graph)
solution = Solution(partition, graph)

bswap = bestSwap(solution)
print(f"Best swap: {bswap}")
# ok

# bestSolution = gradientDescent(graph, 2)
# print(f"Best solution: {bestSolution[0]} with cost {bestSolution[1]}")

# TODO: fix the gradient descent method