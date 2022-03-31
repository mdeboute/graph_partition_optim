import time
from utils import *
from enum import *
from random_partition import *
from neighborhood import *

t = time.time()
graph = parser("./data/dixSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print(verbose=False)

partition = makeBiPartition(graph)
solution = Solution(partition, graph)

bswap = bestSwap(solution)
print(f"Best swap: {bswap[0]} with cost {bswap[1]}")

# print("\n")
# basicEnum(graph)

# print(f"\nSolution: {solution} with cost {solution.getCost()}\n")

# print("\n")