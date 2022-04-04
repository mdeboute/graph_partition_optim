def evaluateur(solution):
    graph = solution.getGraph()
    partition = solution.getPartition()
    nbClasses = solution.getNbClasses()
    cost = 0
    for c in range(nbClasses):
        for c2 in range(nbClasses):
            if c < c2:
                for node in partition[c]:
                    for node2 in partition[c2]:
                        if graph.getEdge(node, node2) is not None:
                            cost += 1

    return cost
