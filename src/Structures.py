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
            + " with weight "
            + str(self.weight)
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
            + " with weight "
            + str(self.weight)
        )

    def __eq__(self, other):
        """
        Returns True if the edges are equal.
        """
        if other == None:
            return False
        return (
            self.source == other.source
            and self.destination == other.destination
            and self.weight == other.weight
        )

    def __hash__(self):
        """
        Returns a hash representation of the edge.
        """
        return hash((self.firstVertex, self.secondVertex, self.weight))


class Graph(Edge):
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
        return hash(
            (
                self.nb_vertices,
                self.nb_edges,
                self.dmin,
                self.dmax,
                self.edges,
                self.degrees,
            )
        )

    def print_graph(self):
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
        print("Degrees: " + str(self.degrees))
        print("Edges:")
        for edge in self.edges:
            print(edge)
        print("")

    def get_edge(self, firstVertex, secondVertex):
        """
        Returns the edge between firstVertex and secondVertex.
        """
        for edge in self.edges:
            if edge.firstVertex == firstVertex and edge.secondVertex == secondVertex:
                return edge
        return None

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


class Solution(Graph):
    def __init__(self, partition, graph, nbClasses=2):
        self.partition = partition
        self.graph = graph
        self.nbClasses = nbClasses

    def __str__(self):
        """
        Returns a string representation of the solution.
        """
        tmp = ""
        for i in range(len(self.partition)):
            tmp += "Partition " + str(i) + ": " + str(self.partition[i]) + "\n"
        return tmp

    def __repr__(self):
        """
        Returns a string representation of the solution.
        """
        tmp = ""
        for i in range(self.graph.nb_vertices):
            tmp += (
                "Node " + str(i) + " assigned to class " + str(self.partition[i]) + "\n"
            )
        return tmp

    def __eq__(self, other):
        """
        Returns True if the graphs are equal.
        """
        return self.partition == other.partition

    def __hash__(self):
        """
        Returns a hash representation of the graph.
        """
        return hash((self.graph, self.nbClasses, self.partition))

    # this method returns the cost of the solution as the sum of the weiths of the inter-class edges
    def get_cost(self):
        """
        Returns the cost of the solution.
        """
        cost = 0
        for i in range(len(self.partition)):
            for j in range(len(self.partition[i])):
                for k in range(j + 1, len(self.partition[i])):
                    edge = self.graph.get_edge(
                        self.partition[i][j], self.partition[i][k]
                    )
                    if edge is not None:
                        cost += edge.weight
        return cost