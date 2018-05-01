#Adrian Saenz
#
#

from Prims import Prims
from prims_functions import G

V = G.vertex_set()
E = G.edge_set()
InitialVertex = int(input("What is your initial vertex of these vertices?:"))
ShowIterations = input("Do want to see the iterations(y/n)?:")
print("")#extra space
Prims(G,InitialVertex,ShowIterations)
