"""
This file should store all functions that
you write which will be needed in the
steps of Prim’s algorithm
"""

import Weighted_Graph as wg

# G is set is set as an object from Weighted_Graph class from Weighted_Graph.py
# test.txt is the graph
G = wg.Weighted_Graph("test.txt")

# This draws the graph using the draw_graph function from Weighted_Graph class
# and test.txt
G.draw_graph()


#This function determines cost of edges between two vertices
def cost(G, e):
    return G.edge_dict()[e]
print("cost function at (0,1)", cost(G,(0,1)))#test


#This functiion initializes a tree with initial vertex as parameter
def initial_tree(initial_vertex):
    return ({initial_vertex}, [])
print(initial_tree(3))#test


#This function uses intitial_tree as a parameter and then checks which
#other vertices are connected to the initial tree
def incident_edges(G, T):
    edges = []
    for e in G.edge_set():
        for V in T[0]:
            if V in e: 
                edges.append(e)
    return [e for e in edges if e not in T[1]]
print(incident_edges(G, initial_tree(0)))#test


#idk what this function is
def valid_incident_edges(G, T):
    edges = []
    for e in incident_edges(G,T):
        if e[0] not in T[0] or e[1] not in T[0]:
            edges.append(e)  
    return edges
print(valid_incident_edges(G, initial_tree(0)))#test


#Picks which edge is the least
def min_valid_incident_edge(G, T):
    valid_edges = valid_incident_edges(G, T)
    min_edge = valid_edges[0]
    for e in valid_edges: 
        if cost(G,e) < cost(G,min_edge):
            min_edge = e       
    return min_edge
print(min_valid_incident_edge(G,initial_tree(3)))#test




