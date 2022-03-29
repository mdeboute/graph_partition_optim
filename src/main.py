from functools import partialmethod
import time
from utils import *
from enum import basicEnum
from algorithms import *

isPrint = 1

t = time.time()
graph = parser("./data/dixSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print()

print("\nEnumeration:")
et = time.time()
basicEnum(graph.getNbVertices(), 2)
print(time.time() - et, "seconds of enum")

partition = makeBiPartition(graph.getNbVertices())
solution = Solution(partition, graph)
print(solution, solution.getCost())
