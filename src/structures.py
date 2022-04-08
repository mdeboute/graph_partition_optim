# This file consist of a set of classes that allows us to represents a non oriented weighted graph.
# Author: Martin Debouté, Lucas Villenave


class Graph:
    """Represents a graph with an adjacency matrix."""

    def __init__(self, nbVertices, nbEdges, edges, degrees):
        self.nbVertices = nbVertices
        self.nbEdges = nbEdges
        self.edges = edges
        self.degrees = degrees

    def __str__(self):
        """
        Returns a string representation of the graph.
        """
        return (
            "Graph with "
            + str(self.nbVertices)
            + " vertices and "
            + str(self.nbEdges)
            + " edges."
        )

    def __repr__(self):
        """
        Returns a string representation of the graph.
        """
        return (
            "Graph with "
            + str(self.nbVertices)
            + " vertices and "
            + str(self.nbEdges)
            + " edges."
        )

    def __eq__(self, other):
        """
        Returns True if the graphs are equal.
        """
        return (
            self.nbVertices == other.nbVertices
            and self.nbEdges == other.nbEdges
            and self.edges == other.edges
            and self.degrees == other.degrees
        )

    def __hash__(self):
        """
        Returns a hash representation of the graph.
        """
        return hash(
            (
                self.nbVertices,
                self.nbEdges,
                self.edges,
                self.degrees,
            )
        )

    def print(self, verbose=False):
        """
        Prints the graph.
        """
        print(
            "Graph with "
            + str(self.nbVertices)
            + " vertices and "
            + str(self.nbEdges)
            + " edges."
        )
        if verbose:
            print("\n")
            print("Edges:")
            # print the edges as an adjacency list (i.e src -> dest, weight)
            # the matrix is symmetric so we only need to print the upper part
            for i in range(self.nbVertices):
                for j in range(i + 1, self.nbVertices):
                    if self.edges[i][j] != 0:
                        print(
                            i + 1, "->", j + 1, ":", self.edges[i][j]
                        )  # i/j + 1 because the matrix is 0-indexed
            print("\n")
            print("Degrees:")
            for i in range(len(self.degrees)):
                print(
                    i + 1, ":", self.degrees[i]
                )  # i+1 because the vertices are indexed from 1
        print("\n")

    def getNbEdges(self):
        """
        Returns the number of edges of the graph.
        """
        return self.nbEdges

    def getNbVertices(self):
        """
        Returns the number of vertices of the graph.
        """
        return self.nbVertices

    def getNeighbors(self, vertex):
        """
        Returns the neighbors of the vertex if it's possible.
        """
        neighbors = []
        for i in range(self.nbVertices):
            if vertex <= self.nbVertices and vertex >= 0:
                if self.edges[vertex][i] != 0:
                    neighbors.append(i)
        return neighbors

    def getEdges(self):
        """
        Returns the edges of the graph.
        """
        return self.edges

    def getDegrees(self):
        """
        Returns the degrees of the graph.
        """
        return self.degrees

    def getDegree(self, vertex):
        """
        Returns the degree of the vertex.
        """
        return self.degrees[vertex]


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

    def getCost(self):
        """
        Returns the cost of the solution as the sum of the weiths of the inter-class edges
        """
        cost = 0
        for i in range(self.nbClasses):
            for j in range(i + 1, self.nbClasses):
                for vertex in self.partition[i]:
                    for neighbor in self.graph.getNeighbors(vertex):
                        if neighbor in self.partition[j]:
                            cost += self.graph.getEdges()[vertex][neighbor]
        return cost

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

    def getNbVerticesInClass(self, _class_):
        """
        Returns the number of vertices in the class.
        """
        return len(self.partition[_class_])

    def getGraph(self):
        """
        Returns the graph of the solution.
        """
        return self.graph

    def isFeasible(self):
        # Check if the solution is feasible
        # The partition is correct if the sum of the number of vertices
        # in each class is equal to the number of vertices of the graph associated to the solution
        # And if the number of vertices in each class is approximatively the same

        feasible = None

        # check the first condition
        count = 0
        nbVertices = self.graph.getNbVertices()
        for i in range(self.nbClasses):
            count += len(self.partition[i])
        if count == nbVertices:
            feasible = True
        else:
            feasible = False

        # check the second condition
        nbVertices_per_class_approx = nbVertices // self.nbClasses
        for i in range(self.nbClasses):
            if len(self.partition[i]) < nbVertices_per_class_approx:
                feasible = False

        return feasible


# TODO: deepen the notion of approximately
