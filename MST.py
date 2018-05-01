#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estefany Lemus

Main program that solves MST
"""

from Prims import Prims
from Prims_functions import G


InitialVertex = int(input("What is your initial vertex of these vertices?:"))
ShowIterations = input("Do want to see the iterations(y/n)?:")

Prims(G,InitialVertex,ShowIterations)

