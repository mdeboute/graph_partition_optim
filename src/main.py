import time
from utils import *
from enum import basicEnum
from random_partition import *
from neighborhood import *

t = time.time()
graph = parser("./data/quinzeSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print()

# partition = makeBiPartition(graph.getNbVertices())
# solution = Solution(partition, graph)

print("\n")
basicEnum(graph)

# print(f"\nSolution: {solution} with cost {solution.getCost()}\n")

print("\n")

# swapVoisinage(solution)

# kpartition = makeKPartition(graph.getNbVertices(), 3)
# ksolution = Solution(kpartition, graph, 3)
# print(kpartition)

# pickNDropVoisinage(ksolution, 0)
