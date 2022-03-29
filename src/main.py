import time
from utils import *
from enum import basicEnum

isPrint = 1

t = time.time()
graph = parser("./data/quatreSommets.txt")
print(time.time() - t, "seconds of parsing")

graph.print()

print("\nEnumeration:")
et = time.time()
basicEnum(graph.getNbVertices(), 2)
print(time.time() - et, "seconds of enum")
