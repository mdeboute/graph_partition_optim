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

partition = makeKPartition(graph, k=2)
solution = Solution(partition, graph, nbClasses=2)
neighborhood = swap(solution)

print(gradientDescent(solution, neighborhood))


# TODO: fix the gradient descent method