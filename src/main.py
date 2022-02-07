from utils import *
import time
from enum import enum
import random


t = time.time()
graph = parser("../data/quatreSommets.txt")
print(time.time() - t, "seconds")
graph.print_graph()

enum(graph.getNbVertices())
