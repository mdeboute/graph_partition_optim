from utils import *
import time
import enum
import algorithms


t = time.time()
graph = parser("../data/dixSommets.txt")
print(time.time() - t, "seconds")
graph.print_graph()

enum.basicEnum(graph.getNbVertices())

partition = algorithms.makeBiPartition(graph.getNbVertices())

sol = Solution(partition, graph, 0)

print(sol, sol.get_cost())