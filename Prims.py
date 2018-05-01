from prims_functions import cost, min_valid_incident_edge, initial_tree,G
import prims_functions as P


V = G.vertex_set()
E = G.edge_set()

def Prims(Graph,InitialVertex,ShowIterations):
    
    
    VT = {InitialVertex} #initial #VT is vertex
    ET = [] #ET is min edge
    Tree = (VT, ET) #MST
    
    edges = P.incident_edges(G,Tree)
    valid_edges = P.valid_incident_edges(G,Tree)#
    min_edge = P.min_valid_incident_edge(G,Tree)#
    new_vertices = {min_edge[0], min_edge[1]}
    cost_min_edge=P.cost(G,P.min_valid_incident_edge(G,Tree))
    
    """Prims alg w/ Iterations"""
    if ShowIterations == "y":
        x=0
        while Tree[0] != V:
            x+=1
            print('Iteration :',x)
            min_edge = P.min_valid_incident_edge(G,Tree)#
            new_vertices = {min_edge[0], min_edge[1]}
            ET.append(min_edge)
            Tree =[new_vertices.union(Tree[0]),ET]
            print("MST:",Tree)
            print("")
    
    
    elif ShowIterations == "n":
        while Tree[0] != V:
            min_edge = P.min_valid_incident_edge(G,Tree)#
            new_vertices = {min_edge[0], min_edge[1]}
            ET.append(min_edge)
            Tree =[new_vertices.union(Tree[0]),ET]
        print("MST:",Tree)
        print("")
   
        
#This shows the min cost of the MST        
    total_cost =0
    for e in Tree[0]:
        total_cost += cost_min_edge
    print ("The total cost of the MST is:",total_cost)
        
