from functools import partialmethod
import time
from utils import *
from enum import basicEnum
from algorithms import *
from neighborhood import *
from evaluateur import *
from descenteDeGradiant import *


k=2

t = time.time()
graph = parser("./data/dixSommets.txt")
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