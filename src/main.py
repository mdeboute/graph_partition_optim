import time
from gradient_descent import gradientDescent
from utils import *
from enum import *
from random_partition import *
from neighborhood import *

t = time.time()
graph = parser("./data/centSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print(verbose=False)

partition = makeBiPartition(graph)
solution = Solution(partition, graph)
neighborhood = swap(solution)

print(solution.getCost())
# print(gradientDescent(solution, neighborhood))


# TODO: fix the gradient descent method