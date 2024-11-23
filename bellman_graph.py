from arc import Arc
import numpy as np


class Bellman_Graph:
    # Constructor
    def __init__(self):
        self.vertices = set()
        self.arcs = list()

    # add a new vertex
    def add_new_vertex(self, new_vertex):
        self.vertices.add(new_vertex)

    # remove a vertex
    def delete_existing_vertex(self, vertex_to_remove):
        # vertex don't exist in the vertices list => message error
        if vertex_to_remove not in self.vertices :
            print("You're trying to delete a non existent vertex :) ")

        # vertex exist in the vertices list => must be removed
        else :
            # remove the vertex
            self.vertices.remove(vertex_to_remove)

            # delete related arcs and reorganize the arcs list
            arcs_list_reorganized = []
            for arc in self.arcs:
                if arc.start != vertex_to_remove and arc.end != vertex_to_remove:
                    arcs_list_reorganized.append(arc)
            self.edges = arcs_list_reorganized
    
    # add a new arc
    def add_new_arc(self, new_arc):
        self.arcs.append(new_arc)
        self.add_new_vertex(new_arc.start)
        self.add_new_vertex(new_arc.end)

    # remove an arc
    def delete_exisitng_arc(self, arc_to_remove):
        # new list of arcs after removing 'arc_to_remove'
        new_arcs = list()
        for arc in self.arcs :
            if arc.start != arc_to_remove.start or arc.end != arc_to_remove.end : 
                new_arcs.append(arc)
        self.arcs = new_arcs
    
    # modify the weight of an arc if it exists
    def modify_weight_arc(self, arc_to_modify, new_weight):
        for arc in self.arcs :
            if arc.start == arc_to_modify.start and arc.end == arc_to_modify.end :
                arc.weight = new_weight
                break

    # Bellman calculation function
    def bellman_algo(self, start):

        # distances set initialization
        distances = {}
        # set all distances element to infinity expect the source
        for vertex in self.vertices :
            distances[vertex] = float('inf')
        distances[start] = 0

        # bellman algo execution
        for _ in range(len(self.vertices) - 1):
            for arc in self.arcs:
                if distances[arc.start] != float('inf') and distances[arc.start] + arc.weight < distances[arc.end]:
                    distances[arc.end] = distances[arc.start] + arc.weight

        # Check for negative weight cycles
        for arc in self.arcs:
            if distances[arc.start] != float('inf') and distances[arc.start] + arc.weight < distances[arc.end]:
                raise ValueError("Graph contains a negative weight cycle.")

        return distances

""" Activate the code below to test """
"""
# Create instances of the Bellman_Graph and Arc classes
graph = Bellman_Graph()

# Add vertices
graph.add_new_vertex('A')
graph.add_new_vertex('B')
graph.add_new_vertex('C')
graph.add_new_vertex('D')

# Add arcs (edges) with weights
graph.add_new_arc(Arc('A', 'B', 4))
graph.add_new_arc(Arc('A', 'C', 2))
graph.add_new_arc(Arc('B', 'C', 5))
graph.add_new_arc(Arc('B', 'D', 10))
graph.add_new_arc(Arc('C', 'D', 3))

# Print the graph's arcs
print("Arcs in the graph:")
for arc in graph.arcs:
    print(f"From {arc.start} to {arc.end} with weight {arc.weight}")

# Test Bellman-Ford Algorithm from source 'A'
print("\nTesting Bellman-Ford Algorithm from source 'A':")
distances_from_A = graph.bellman_algo('A')
print(distances_from_A)  # Expected shortest paths from A to all other vertices

# Test Bellman-Ford Algorithm from source 'B'
print("\nTesting Bellman-Ford Algorithm from source 'B':")
distances_from_B = graph.bellman_algo('B')
print(distances_from_B)  # Expected shortest paths from B to all other vertices
"""