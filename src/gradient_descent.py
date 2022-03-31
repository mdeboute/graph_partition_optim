from neighborhood import *
from random_partition import *


def gradientDescent(graph, k=2):
    """
    Returns the best solution using the swap for the neighborhood.
    @param graph: the graph
    @param k: the number of classes
    @return: the best solution of the graph
    """
    partition = makeKPartition(graph, k)
    champion = Solution(partition, graph, k)
    championPower = champion.getCost()
    isHavingFun = True  # yay!
    challenger = None
    while isHavingFun:
        isHavingFun = False  # ho...
        challenger = Solution(bestSwap(champion), graph, k)  # a new challenger arise
        challengerPower = challenger.getCost()

        if challengerPower < championPower:  # champion is slain
            isHavingFun = True  # bloodbath yay
            champion = challenger  # new champion is crown
    return champion, championPower
