#Adrian Saenz
#Estefany Lemus
#Ary Hernandez

from prims_functions import G
import prims_functions as P


V = G.vertex_set()

def Prims(Graph,Initial_Vertex,Show_Iteration):
    
    #initilization, tuples
    VT = {Initial_Vertex} 
    ET = [] 
    MST = (VT, ET) 
    
    cost_min_edge=P.cost(G,P.min_valid_incident_edge(G,MST))
    
    '''PRIMS ALGORITHM'''
    # w/ iterations
    if Show_Iteration == 'yes':
        x=0
        while MST[0] != V:
            x+=1
            print('Iteration :',x)
            min_edge = P.min_valid_incident_edge(G,MST)
            new_vertex = {min_edge[0], min_edge[1]}
            
            ET.append(min_edge)
            MST =[new_vertex.union(MST[0]),ET]
            print('MST:',MST , '\n ')
           
        total_cost =0
        for e in MST[0]:
            total_cost += cost_min_edge
        print ('\n', 'The total cost of the MST is:',total_cost, '\n')
        
    # w/o iterations
    elif Show_Iteration == 'no':
        while MST[0] != V:
            min_edge = P.min_valid_incident_edge(G,MST)
            new_vertex = {min_edge[0], min_edge[1]}
            
            ET.append(min_edge)
            MST =[new_vertex.union(MST[0]),ET]
        print('MST:',MST, '\n')
       
        total_cost =0
        for e in MST[0]:
            total_cost += cost_min_edge
        print ('\n', 'Total cost of MST:', total_cost, '\n')
        
       
    print ('Minimum Spanning Tree SubGraph:')
    G.draw_subgraph(MST)
