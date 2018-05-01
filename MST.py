#Adrian Saenz
#Estefany Lemus
#

from prims import Prims
from prims_functions import G


InitialVertex = int(input("Enter the vertex where you wish to begin? "))
ShowIterations = input("Would you like to see the iterated path (y/n) ? ")

Prims(G,InitialVertex,ShowIterations)
