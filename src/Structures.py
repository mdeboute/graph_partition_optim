# This file consist of a set of classes that allows us to represents a non oriented weighted graph.
# Author: Martin Debouté, Lucas Villenave


class Edge:
    """
    Represents an edge of a graph.
    """

    def __init__(self, firstVertex, secondVertex, weight):
        self.firstVertex = firstVertex
        self.secondVertex = secondVertex
        self.weight = weight

    def __str__(self):
        """
        Returns a string representation of the edge.
        """
        return (
            "Edge from "
            + str(self.firstVertex)
            + " to "
            + str(self.secondVertex)
            # + " with weight "
            # + str(self.weight)
            # all the weights are equal to 1
        )

    def __repr__(self):
        """
        Returns a string representation of the edge.
        """
        return (
            "Edge from "
            + str(self.firstVertex)
            + " to "
            + str(self.secondVertex)
            # + " with weight "
            # + str(self.weight)
            # all the weights are equal to 1
        )

    def __eq__(self, other):
        """
        Returns True if the edges are equal.
        """
        return (
            self.firstVertex == other.firstVertex
            and self.secondVertex == other.secondVertex
            and self.weight == other.weight
        )

    def __hash__(self):
        """
        Returns a hash representation of the edge.
        """
        return hash(self.firstVertex) ^ hash(self.secondVertex) ^ hash(self.weight)


class Graph(Edge):
    """Represents a graph"""

    def __init__(self, nb_vertices, nb_edges, dmin, dmax, edges, degrees):
        self.nb_vertices = nb_vertices
        self.nb_edges = nb_edges
        self.dmin = dmin
        self.dmax = dmax
        self.edges = edges
        self.degrees = degrees

    def __str__(self):
        """
        Returns a string representation of the graph.
        """
        return (
            "Graph with "
            + str(self.nb_vertices)
            + " vertices and "
            + str(self.nb_edges)
            + " edges."
        )

    def __repr__(self):
        """
        Returns a string representation of the graph.
        """
        return (
            "Graph with "
            + str(self.nb_vertices)
            + " vertices and "
            + str(self.nb_edges)
            + " edges."
        )

    def __eq__(self, other):
        """
        Returns True if the graphs are equal.
        """
        return (
            self.nb_vertices == other.nb_vertices
            and self.nb_edges == other.nb_edges
            and self.dmin == other.dmin
            and self.dmax == other.dmax
            and self.edges == other.edges
            and self.degrees == other.degrees
        )

    def __hash__(self):
        """
        Returns a hash representation of the graph.
        """
        return (
            hash(self.nb_vertices)
            ^ hash(self.nb_edges)
            ^ hash(self.dmin)
            ^ hash(self.dmax)
        )

    def print(self):
        """
        Prints the graph.
        """
        print(
            "Graph with "
            + str(self.nb_vertices)
            + " vertices and "
            + str(self.nb_edges)
            + " edges."
        )
        print("\n")
        print("Edges:")
        for edge in self.edges:
            print(edge)
        print("\n")
        print("Degrees:")
        for i in range(len(self.degrees)):
            print(i + 1, ":", self.degrees[i])

    def getEdge(self, firstVertex, secondVertex):
        """
        Returns the edge between firstVertex and secondVertex.
        """
        for edge in self.edges:
            if (
                edge.firstVertex == firstVertex and edge.secondVertex == secondVertex
            ) or (
                edge.firstVertex == secondVertex and edge.secondVertex == firstVertex
            ):
                return edge

    def getNbEdges(self):
        """
        Returns the number of edges of the graph.
        """
        return self.nb_edges

    def getNbVertices(self):
        """
        Returns the number of vertices of the graph.
        """
        return self.nb_vertices

    def has_key(self, vertex):
        """
        Returns True if the graph has the vertex.
        """
        return vertex in self.degrees

    def getNeighbors(self, vertex):
        """
        Returns the neighbors of the vertex.
        """
        neighbors = []
        for edge in self.edges:
            if edge.firstVertex == vertex:
                neighbors.append(edge.secondVertex)
            if edge.secondVertex == vertex:
                neighbors.append(edge.firstVertex)
        return neighbors


class Solution(Graph):
    """Represents a solution"""

    def __init__(self, partition, graph, nbClasses=2):
        self.partition = partition
        self.graph = graph
        self.nbClasses = nbClasses

    def __str__(self):
        """
        Returns a string representation of the solution.
        """
        return str(self.partition)

    def __repr__(self):
        """
        Returns a string representation of the solution.
        """
        return str(self.partition)

    def __eq__(self, other):
        """
        Returns True if the solutions are equal.
        """
        return (
            self.graph == other.graph
            and self.nbClasses == other.nbClasses
            and self.partition == other.partition
        )

    def __hash__(self):
        """
        Returns a hash representation of the solution.
        """
        return hash(self.graph) ^ hash(self.nbClasses) ^ hash(self.partition)

    # this method returns the cost of the solution as the sum of the weiths of the inter-class edges
    def getCost(self):
        """
        Returns the cost of the solution.
        """
        cost = 0
        for i in range(self.nbClasses):
            for vertex in self.partition[i]:
                for neighbor in self.graph.getNeighbors(vertex):
                    if self.partition[i].count(neighbor) == 0:
                        if self.graph.getEdge(vertex, neighbor) is not None:
                            cost += self.graph.getEdge(vertex, neighbor).weight
        return cost // 2

    def getNbClasses(self):
        """
        Returns the number of classes of the solution.
        """
        return self.nbClasses

    def getPartition(self):
        """
        Returns the partition of the solution.
        """
        return self.partition

    def getNbVerticesInClass(self, class_):
        """
        Returns the number of vertices in the class.
        """
        return len(self.partition[class_])

    def getGraph(self):
        """
        Returns the graph of the solution.
        """
        return self.graph