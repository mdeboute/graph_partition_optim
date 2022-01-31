# This file consist of a set of classes that allows us to represents a non oriented weighted graph.
# Author: Martin Debouté


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
        return "Edge from " + str(self.firstVertex) + " to " + str(self.secondVertex) + " with weight " + str(self.weight)

    def __repr__(self):
        """
        Returns a string representation of the edge.
        """
        return "Edge from " + str(self.firstVertex) + " to " + str(self.secondVertex) + " with weight " + str(self.weight)

    def __eq__(self, other):
        """
        Returns True if the edges are equal.
        """
        return self.firstVertex == other.firstVertex and self.secondVertex == other.secondVertex and self.weight == other.weight

    def __hash__(self):
        """
        Returns a hash representation of the edge.
        """
        return hash((self.firstVertex, self.secondVertex, self.weight))


class Graph:
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
        return "Graph with " + str(self.nb_vertices) + " vertices and " + str(self.nb_edges) + " edges."

    def __repr__(self):
        """
        Returns a string representation of the graph.
        """
        return "Graph with " + str(self.nb_vertices) + " vertices and " + str(self.nb_edges) + " edges."

    def __eq__(self, other):
        """
        Returns True if the graphs are equal.
        """
        return self.nb_vertices == other.nb_vertices and self.nb_edges == other.nb_edges and self.dmin == other.dmin and self.dmax == other.dmax and self.edges == other.edges and self.degrees == other.degrees

    def __hash__(self):
        """
        Returns a hash representation of the graph.
        """
        return hash((self.nb_vertices, self.nb_edges, self.dmin, self.dmax, self.edges, self.degrees))

    def print_graph(self):
        """
        Prints the graph.
        """
        print("Graph with " + str(self.nb_vertices) + " vertices and " + str(self.nb_edges) + " edges.")
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
