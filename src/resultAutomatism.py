import time
from enumeration import basicEnum
from utils import *
from metaheuristics import *
from main import initSol
from gradient_descent import *

# global basic params  
k = 2
neighborhoodSize = 100
iterMax = 1 # will be multiplyed by nbVertices
timeOut = 6
tabuSize = 7
temperature = 36
coolingRate = 0.09
finalTemperature = 0.01

doEnum = False

doGradient = True
doBetterGradient = False
doTabou = False
doTabouNSwap = False
doRC = False
doNSwapRC = False

isInitSol = doGradient or doBetterGradient or doTabou or doTabouNSwap or doRC or doNSwapRC

def resultAutomatism() :
    
    #comment the ones you don't want to use
    instances = [
        "data/quatreSommets.txt",
        "data/cinqSommets.txt",
        "data/dixSommets.txt",
        "data/quinzeSommets.txt",
        "data/dixSeptSommets.txt",
        "data/vingtSommets.txt",
        "data/vingtEtunSommets.txt",
        "data/vingtDeuxSommets.txt",
        "data/vingtTroisSommets.txt",
        "data/vingtQuatreSommets.txt",
        "data/vingtCinqSommets.txt",
        "data/trenteSommets.txt",
        "data/cinquanteSommets.txt",
        "data/centSommets.txt",
        "data/cinqCentSommets.txt",
        "data/milleSommets.txt",
        "data/dixMilleSommets.txt",
    ]
    for i in range (2,5) : 
        k = i
        for path in instances :
            do(path,k,neighborhoodSize,iterMax,timeOut,tabuSize)

def do(path,k,neighborhoodSize,iterMax,timeOut,tabuSize) :
    
    print("\n##################\n\n                 Instance : ", path,"\n")
    print("                 with k = ",k,"\n")
    t = time.time()
    graph = parse(path)
    
    if isInitSol :
        initialSolution, initialSolutionCost = initSol(graph,k)
    
    if doTabou :
        t = time.time()
        sol,solCost = tabuSearch( initialSolution, initialSolutionCost, iterMax*graph.getNbVertices(), timeOut, tabuSize, False, neighborhoodSize, False,)
        print("\nTabou found the solution : ",sol," with a cost of ",solCost, " in ", time.time()-t,"seconds.")
        
    if doTabouNSwap :
        t = time.time()
        sol,solCost = tabuSearch( initialSolution, initialSolutionCost, iterMax*graph.getNbVertices(), timeOut, tabuSize, True, neighborhoodSize, True,)
        print("\nTabou nSwap found the solution : ",sol," with a cost of ",solCost, " in ", time.time()-t,"seconds.")
    
    if doGradient :
        t = time.time()
        sol,solCost = gradientDescent( initialSolution, initialSolutionCost, timeOut+time.time(), False, neighborhoodSize)
        print("\nGD found the solution : ",sol," with a cost of ",solCost, " in ", time.time()-t,"seconds.")
        
    if doBetterGradient :
        t = time.time()
        sol,solCost = betterGradientDescent( initialSolution, initialSolutionCost, timeOut+time.time(), False, neighborhoodSize)
        print("\nbetterGD found the solution : ",sol," with a cost of ",solCost, " in ", time.time()-t,"seconds.")
        
    if doRC :
        t = time.time()
        sol,solCost = simulatedAnnealing( initialSolution, initialSolutionCost, swapNodes(initialSolution), iterMax*graph.getNbVertices(), timeOut, False, neighborhoodSize, temperature, finalTemperature, coolingRate)
        print("\RC found the solution : ",sol," with a cost of ",solCost, " in ", time.time()-t,"seconds.")
    
    if doNSwapRC :
        t = time.time()
        sol,solCost = simulatedAnnealing( initialSolution, initialSolutionCost, swapNodes(initialSolution), iterMax*graph.getNbVertices(), timeOut, True, neighborhoodSize, temperature, finalTemperature, coolingRate)
        print("\RC found the solution : ",sol," with a cost of ",solCost, " in ", time.time()-t,"seconds.")
    
    if doEnum :
        t = time.time()
        sol,solCost = basicEnum( graph, timeOut, k)
        print("\nEnum found the solution : ",sol," with a cost of ",solCost, " in ", time.time()-t,"seconds.")

if __name__ == "__main__":
    resultAutomatism()