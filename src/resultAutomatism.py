import time
from utils import *
from metaheuristics import *
from main import initSol

# global basic params  
k = 2
neighborhoodSize = 100
iterMax = 1 # will be multiplyed by nbVertices
timeOut = 600
tabuSize = 7

doEnum = False

doGradient = False
doBetterGradient = False
doTabou = True
doTabouNSwap = True

def resultAutomatism() :
    
    #comment the ones you don't want to use
    instances = [
        #"data/quatreSommets.txt",
        #"data/cinqSommets.txt",
        #"data/dixSommets.txt",
        #"data/quinzeSommets.txt",
        #"data/dixSeptSommets.txt",
        #"data/vingtSommets.txt",
        #"data/vingtEtunSommets.txt",
        #"data/vingtDeuxSommets.txt",
        #"data/vingtTroisSommets.txt",
        #"data/vingtQuatreSommets.txt",
        #"data/vingtCinqSommets.txt",
        #"data/trenteSommets.txt",
        #"data/cinquanteSommets.txt",
        "data/centSommets.txt",
        #"data/cinqCentSommets.txt",
        #"data/milleSommets.txt",
        #"data/dixMilleSommets.txt",
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
    
    initialSolution, initialSolutionCost = initSol(graph,k)
    
    #Tabou
    t = time.time()
    sol,solCost = tabuSearch( initialSolution, initialSolutionCost, iterMax*graph.getNbVertices(), timeOut, tabuSize, True, neighborhoodSize, True,)
    print("\nTabou found the solution : ",sol," with a cost of ",solCost, " in ", time.time()-t,"seconds.")

if __name__ == "__main__":
    resultAutomatism()