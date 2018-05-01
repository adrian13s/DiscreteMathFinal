#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estefany Lemus

Main program that solves MST
"""

from Prims import Prims
from Prims_functions import G


V = G.vertex_set()
E = G.edge_set()

Initial_Vertex = int(input('Enter the vertex where you wish to begin: '))
Show_Iterations = eval(input('Do want to see the iterations (y/n)?: '))

Prims(G,Initial_Vertex,Show_Iterations, Show_Cost)

