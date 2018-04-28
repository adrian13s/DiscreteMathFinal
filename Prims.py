#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 18:46:21 2018

"""

from prims_functions import cost, min_valid_incident_edge, initial_tree


def Prims(G, T):
  MST = []
  new_vertex = []
  V = G.edge_set()
  X = G.vertex_set()
  X.append(initial_tree(3)) #initialization
  while X[0] != V: 
     
      for X[0] in (V):
          e = min_valid_incident_edge(X) #finds smallest edge
          MST.append(e) #Adds min edge
          new_vertex.append(cost(e)) #Adds cost to new vertex
          
          for e in MST: #print edges of MST
              print (MST)
          
    
 

                  
               
                    
            
                
        
        
        



        
        
       
        
    


