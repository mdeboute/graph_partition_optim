import time
from utils import *
from enum import enum2

isPrint = 1

t = time.time()
graph = parser("../data/dixSommets.txt")
print(time.time() - t, "seconds of parsing")

if isPrint:
    graph.print_graph()

et = time.time()
enum2(graph, isPrint, 2)
print(time.time() - et, "seconds of enum")
