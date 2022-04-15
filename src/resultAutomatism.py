import time
from utils import *
from metaheuristics import *
from main import initSol

def resultAutomatism() :
    
    # global basic params  
    k = 2
    neighborhoodSize = 100
    iterMax = 1 # will be multiplyed by nbVertices
    timeOut = 600
    tabuSize = 7
    
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
        #"data/dixMilleSommets.txt",
    ]
    
    for path in instances :
        t = time.time()
        graph = parse(path)
        print ("successfully parsed in ", time.time()-t, "seconds")
        
        print(path)
        initialSolution, initialSolutionCost = initSol(graph,k)
        
        #Tabou
        t = time.time()
        sol,solCost = tabuSearch( initialSolution, initialSolutionCost, iterMax*graph.getNbVertices(), timeOut, tabuSize, False, neighborhoodSize, False,)
        print("Tabou found the solution : ",sol," with a cost of ",solCost, " in ", time.time()-t,"seconds.")
    
if __name__ == "__main__":
    resultAutomatism()