from utils import *
import time

t = time.time()
graph = parser("../data/dixSommets.txt")
print(time.time() - t, "seconds")
graph.print_graph()
