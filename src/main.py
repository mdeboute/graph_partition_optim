import time, sys
from enumeration import basicEnum
from gradient_descent import *
from utils import *
from enum import *
from neighborhood import *
from metaheuristics import *


def initSol(graph, k=2):
    """
    Returns an initial solution.
    @param graph: the graph
    @param k: the number of classes
    @return: the initial solution and its cost
    """

    partition = makeKPartition(graph, nbClasses=k)
    solution = Solution(partition, graph, nbClasses=k)
    t = time.time()
    solutionCost = solution.getCost()
    print(
        f"Initial solution cost: {solutionCost}, computed in: {time.time() - t:.2f} seconds."
    )
    return solution, solutionCost


def main():
    # CLI arguments will be used to set the parameters of the algorithm as follows:
    #   -h, --help: print this help message
    #   -e, --enum: perform basic enumeration
    #   -g, --gradient: perform gradient descent
    #   -m1, --meta1: perform simulated annealing
    #   -m2, --meta2: perform tabu search
    #   -t, --time: set the time limit for the algorithm in seconds (default: 600)
    #   -c, --class: set the number of classes to be considered (default: 2)
    #   -s, --size: set the size of the neighborhood (default: all the neighborhood)
    # only for gradient descent or metaheuristics.

    args = sys.argv[1:]

    if len(args) == 0:
        print("No arguments provided. Please use -h for help.")
        return

    if len(args) > 9:
        print("Too many arguments provided. Please use -h for help.")
        return

    if "-h" in args or "--help" in args:
        print("Usage: python3 main.py [filePath] [options]")
        print("Options:")
        print("  -h, --help: print this help message")
        print("  -e, --enum: perform basic enumeration")
        print("  -g, --gradient: perform gradient descent")
        print("  -m1, --meta1: perform simulated annealing")
        print("  -m2, --meta2: perform tabu search")
        print("  -t, --time: set the time limit for the algorithm (default: 600)")
        print("  -c, --class: set the number of classes to be considered (default: 2)")
        print(
            "  -s, --size: set a size for the neighborhood (default: all the neighborhood)",
            "only for gradient descent or metaheuristics.",
        )
        return

    filePath = args[0]
    t = time.time()
    graph = parse(filePath)
    print(f"Graph created in: {time.time() - t:.2f} seconds.")
    graph.print(verbose=False)

    if "-e" in args or "--enum" in args:
        if "-t" in args or "--time" in args:
            timeLimit = int(args[args.index("-t") + 1])
        else:
            timeLimit = 600
        if "-c" in args or "--c" in args:
            k = int(args[args.index("-c") + 1])
        else:
            k = 2
        bestSol, bestCost = basicEnum(graph, timeLimit, k)
        print(f"Best solution: {bestSol}")
        print(
            f"Result: best solution found in {time.time() - t:.2f} seconds with cost: {bestCost}."
        )

    if "-g" in args or "--gradient" in args:
        if "-t" in args or "--time" in args:
            timeLimit = int(args[args.index("-t") + 1])
        else:
            timeLimit = 600
        if "-c" in args or "--c" in args:
            k = int(args[args.index("-c") + 1])
        else:
            k = 2
        solution, solutionCost = initSol(graph, k)
        if "-s" in args or "--size" in args:
            size = int(args[args.index("-s") + 1])
            bestSol, bestCost = gradientDescent(
                solution,
                solutionCost,
                timeOut=timeLimit + time.time(),  # because it's a recursive function
                nswap=True,
                neighborhoodSize=size,
            )
            print(f"Best solution: {bestSol}")
            print(
                f"Result: best solution found in {time.time() - t:.2f} seconds with cost: {bestCost}."
            )
        else:
            bestSol, bestCost = gradientDescent(
                solution,
                solutionCost,
                timeOut=timeLimit + time.time(),  # because it's a recursive function
                nswap=False,
                neighborhoodSize=None,
            )
            print(f"Best solution: {bestSol}")
            print(
                f"Result: best solution found in {time.time() - t:.2f} seconds with cost: {bestCost}."
            )

    if "-m1" in args or "--meta1" in args:
        if "-t" in args or "--time" in args:
            timeLimit = int(args[args.index("-t") + 1])
        else:
            timeLimit = 600
        if "-c" in args or "--c" in args:
            k = int(args[args.index("-c") + 1])
        else:
            k = 2
        solution, solutionCost = initSol(graph, k)
        if "-s" in args or "--size" in args:
            size = int(args[args.index("-s") + 1])
            bestSol, bestCost = simulatedAnnealing(
                solution,
                solutionCost,
                neighborhood=nSwap(solution, n=size),
                maxIterations=graph.getNbVertices() * 10,
                timeOut=timeLimit,
                nswap=True,
                neighborhoodSize=size,
                initialTemperature=36,
                finalTemperature=0.01,
                coolingRate=0.09,
            )
            print(f"Best solution: {bestSol}")
            print(
                f"Result: best solution found in {time.time() - t:.2f} seconds with cost: {bestCost}."
            )
        else:
            bestSol, bestCost = simulatedAnnealing(
                solution,
                solutionCost,
                neighborhood=swapNodes(solution),
                maxIterations=graph.getNbVertices() * 10,
                timeOut=timeLimit,
                nswap=False,
                neighborhoodSize=None,
                initialTemperature=36,
                finalTemperature=0.01,
                coolingRate=0.09,
            )
            print(f"Best solution: {bestSol}")
            print(
                f"Result: best solution found in {time.time() - t:.2f} seconds with cost: {bestCost}."
            )

    if "-m2" in args or "--meta2" in args:
        if "-t" in args or "--time" in args:
            timeLimit = int(args[args.index("-t") + 1])
        else:
            timeLimit = 600
        if "-c" in args or "--c" in args:
            k = int(args[args.index("-c") + 1])
        else:
            k = 2
        solution, solutionCost = initSol(graph, k)
        if "-s" in args or "--size" in args:
            size = int(args[args.index("-s") + 1])
            bestSol, bestCost = tabuSearch(
                solution,
                solutionCost,
                iterMax=graph.getNbVertices(),
                timeOut=timeLimit,
                tabuSize=7,
                nswap=True,
                neighborhoodSize=size,
                isAspirating=False,
            )
            print(f"Best solution: {bestSol}")
            print(
                f"Result: best solution found in {time.time() - t:.2f} seconds with cost: {bestCost}."
            )
        else:
            bestSol, bestCost = tabuSearch(
                solution,
                solutionCost,
                iterMax=graph.getNbVertices(),
                timeOut=timeLimit,
                tabuSize=7,
                nswap=False,
                neighborhoodSize=None,
                isAspirating=False,
            )
            print(f"Best solution: {bestSol}")
            print(
                f"Result: best solution found in {time.time() - t:.2f} seconds with cost: {bestCost}."
            )


# you should set isAspirating to True if you want to use the aspiration criterion for the tabu search (better results)

if __name__ == "__main__":
    main()
