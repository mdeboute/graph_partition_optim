from main import initSol
from utils import parse, matrixToList, getCost
import time
from genetic import GeneticAlgorithm
from gradient_descent import gradientDescent


graph = parse("./data/cinqCentSommets.txt")
k = 2
solution, solutionCost = initSol(graph, k)
print(f"Inital solution with cost: {solutionCost}")


l = matrixToList(solution.getPartition(), graph.getNbVertices())


def fitness_function(l):
    return getCost(l, graph)


def init():
    sol, solCost = initSol(graph, k)
    return matrixToList(sol.getPartition(), graph.getNbVertices())


ga = GeneticAlgorithm(
    init_function=init,
    population_size=100,
    crossover_rate=0.9,
    mutation_rate=1 / (graph.getNbVertices()),
    max_generations=100,
    fitness_function=fitness_function,
)

start = time.time()
bestSol, bestCost = ga.run()
end = time.time()

print(
    f"Genetic Algorithm: best solution found in {end - start:.4f} seconds with cost: {bestCost}."
)

start = time.time()
bestSol, bestCost = gradientDescent(
    solution,
    solutionCost,
    timeOut=600 + time.time(),
)
end = time.time()

print(
    f"Gradient Descent: best solution found in {end - start:.4f} seconds with cost: {bestCost}."
)
