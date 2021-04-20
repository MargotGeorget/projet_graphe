###import librairies
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from outils_matrices import*
from fonctions_generales import*
from fonctions_distances import*

print("\nTest fonction distances_capitales_frontalières: "
      "\nRetourne toutes les capitales frontalières à la capitale entrée en "
      "paramètre ainsi que leur distances en km les séparant de la capitale")

print("\nTest avec Madrid:")
print(distances_capitales_frontalieres ("Madrid"))

print("\nTest avec Oslo:")
print(distances_capitales_frontalieres ("Oslo"))

print("\nTest avec Berlin:")
print(distances_capitales_frontalieres ("Berlin"))

print("___________________________________________________________________")
print("\nTest fonction distances_min_capitales_frontalières: "
      "\nretourne la capitale frontalière la plus proche de la capitale"
      "entrée en paramètre")

print("\nTest avec Madrid:")
print(distances_min_capitales_frontalieres ("Madrid"))

print("\nTest avec Oslo:")
print(distances_min_capitales_frontalieres ("Oslo"))

print("\nTest avec Berlin:")
print(distances_min_capitales_frontalieres ("Berlin"))

print("___________________________________________________________________")
print("\nTest fonction distances_inferieures_capitales_frontalières: "
      "\nRetourne les capitales frontalières à une distance infèrieur à la "
      "distance entrée en paramètre de la capitale entrée en paramètre")

print("\nTest avec Madrid,800:")
print(distances_inferieures_capitales_frontalieres ("Madrid",800))

print("\nTest avec Oslo,500:")
print(distances_inferieures_capitales_frontalieres ("Oslo",500))

print("\nTest avec Berlin,750:")
print(distances_inferieures_capitales_frontalieres ("Berlin",750))

print("\nTest avec Berlin,450:")
print(distances_inferieures_capitales_frontalieres ("Berlin",450))

#La fonction distance_trajet(chemin) est testé dans le fichier test 
#plus_courte_distance
