#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estefany Lemus
Adrian Saenz
Ary Hernandez
"""
import Weighted_Graph as wg

G = wg.Weighted_Graph("test.txt")

G.draw_graph()

def cost(G, e):
    return G.edge_dict()[e]

#initialization
#incident edges to parameter
def incident_edges(G, T):
    edges = []
    for e in G.edge_set():
        for V in T[0]:
            if V in e: 
                edges.append(e)
    return [e for e in edges if e not in T[1]]

#Functions avoids the graph being cyclical
def valid_incident_edges(G, T):
    edges = []
    for e in incident_edges(G,T):
        if e[0] not in T[0] or e[1] not in T[0]:
            edges.append(e)  
    return edges

#Chooses the min cost edge
def min_valid_incident_edge(G, T):
    valid_edges = valid_incident_edges(G, T)
    min_edge = valid_edges[0]
    for e in valid_edges: 
        if cost(G,e) < cost(G,min_edge):
            min_edge = e       
    return min_edge
