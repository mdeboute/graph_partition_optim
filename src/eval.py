
def eval (graph,partition,nbClasses) :
    cost = 0
    for c in range(nbClasses) :
        for c2 in range(nbClasses) :
            if (c<c2) :
                for node in partition[c] :
                    for node2 in partition[c2] :
                        print (node, " ",node2)
                        if (graph.get_edge(node,node2)!=None) :
                            cost+=1
                            
    return cost

