import arc
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
        self.arcs.add(new_arc)
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
    
    


    




    
