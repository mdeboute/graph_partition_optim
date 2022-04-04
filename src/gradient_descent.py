from neighborhood import *
from random_partition import *

def DescenteDeGradiant (soluce) :
    k = soluce.getNbClasses
    champion = soluce.getPartition()
    championPower = evaluateur(soluce)

    isHavingFun = 1 # yay !

    challenger = []

    challengerPower = -1

    while (isHavingFun == 1) :
        isHavingFun = 0 # ho...

        challenger = bestSwapVoisinage(soluce) # a new challenger arise
        equippedChallenger = Solution(challenger,soluce.getGraph(),soluce.getNbClasses())
        challengerPower = evaluateur(equippedChallenger)

        if (challengerPower < championPower) :
            print("descente")
            isHavingFun = 1 # bloodbath yay
            champion = challenger # new champion is crown
            championPower = challengerPower

    return champion