import time
from utils import *
from enum import basicEnum
from random_partition import *
from neighborhood import *
from evaluateur import *
from gradient_descent import *


k=3

t = time.time()
graph = parser("./data/trenteSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print()

print("\npartition")
et = time.time()

kpartition = makeKPartition(graph.getNbVertices(),k)
ksolution = Solution(kpartition, graph,k)
print(kpartition, " with a cost of ",evaluateur(ksolution))

opt = Solution(DescenteDeGradiant(ksolution),graph,k)

ev = evaluateur(opt)
print("optimal ",opt.getPartition(), " with cost ", ev)

# pickNDropVoisinage(ksolution,0)
