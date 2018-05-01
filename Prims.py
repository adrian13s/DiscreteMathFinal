#Adrian Saenz
#Estefany Lemus
#

from prims_functions import G
import prims_functions as P


V = G.vertex_set()

def Prims(Graph,Initial_Vertex,Show_Iteration):
    
    
    VT = {Initial_Vertex} 
    ET = [] 
    Tree = (VT, ET) 
    
    min_edge = P.min_valid_incident_edge(G,Tree)
    new_vertex = {min_edge[0], min_edge[1]}
    cost_min_edge=P.cost(G,P.min_valid_incident_edge(G,Tree))
    
   
    # w iterations
    if Show_Iteration == "yes":
        x=0
        while Tree[0] != V:
            x+=1
            print('Iteration :',x)
            min_edge = P.min_valid_incident_edge(G,Tree)#
            new_vertex = {min_edge[0], min_edge[1]}
            ET.append(min_edge)
            Tree =[new_vertex.union(Tree[0]),ET]
            print("MST:",Tree)
            print("")
        total_cost =0
        for e in Tree[0]:
            total_cost += cost_min_edge
        print ("The total cost of the MST is:",total_cost)
        
    # w/o iterations
    elif Show_Iteration == "no":
        while Tree[0] != V:
            min_edge = P.min_valid_incident_edge(G,Tree)
            new_vertex = {min_edge[0], min_edge[1]}
            ET.append(min_edge)
            Tree =[new_vertex.union(Tree[0]),ET]
        print("MST:",Tree)
        print("")
        total_cost =0
        
        for e in Tree[0]:
            total_cost += cost_min_edge
        print ("Total cost of MST:", total_cost)
        
    print("")   
    print ("Minimum Spanning Tree SubGraph:")
    G.draw_subgraph(Tree)
