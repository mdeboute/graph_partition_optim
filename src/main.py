from functools import partialmethod
import time
from utils import *
from enum import basicEnum
from algorithms import *
from neighborhood import *

t = time.time()
graph = parser("./data/dixSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print()

print("\nEnumeration:")
et = time.time()

# partition = makeBiPartition(graph.getNbVertices())
# solution = Solution(partition, graph)
# print(solution, solution.getCost())

# swapVoisinage(solution)

kpartition = makeKPartition(graph.getNbVertices(),3)
ksolution = Solution(kpartition, graph,3)
print(kpartition)

pickNDropVoisinage(ksolution,0)
