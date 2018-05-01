#Adrian Saenz
#Estefany Lemus
#

from prims import Prims
from prims_functions import G


Initial_Vertex = int(input("Enter the vertex where you wish to begin? "))
Show_Iteration = eval(input("Would you like to see the iterated path (yes/no) ? "))

Prims(G,Initial_Vertex,Show_Iteration)
