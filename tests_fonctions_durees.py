"""

Ce fichier contient l'ensemble des tests de chaque fonctions se trouvant dans le fichier
"fonctions_durees.py"

"""


#Import librairies
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Import des fonctions

from fonctions_durees import *

print("")
print("Tests de accessible_capitals")
print("Berlin, duree 600:")
print(accessible_capitals("Berlin", 600))
print("\nOslo, duree 200:")
print(accessible_capitals("Oslo", 200))
print("\nParis, duree 300:")
print(accessible_capitals("Paris", 300))

print("")

print("")
print("------------------")
print("Test de border_capitals")
print(border_capitals("Berlin"))
print("\nTallinn:")
print(border_capitals("Tallinn"))
print("")

print("")
print("------------------")
print("Test de nearest_border_capital")
print("Berlin:")
print(nearest_border_capital("Berlin"))
print("\nTallinn:")
print(nearest_border_capital("Tallinn"))
print("")

print("")
print("------------------")
print("Test de exist_path_between_two_capitals")
print("Entre Berlin et Paris:")
print(exist_path_between_two_capitals("Berlin", "Paris"))
print("\nEntre Oslo et Berne:")
print(exist_path_between_two_capitals("Oslo", "Berne"))
print("")

print("")
print("------------------")
print("Test de path_duration_between_two_capitals")
print("Entre Berlin et Paris:")
print(path_duration_between_two_capitals("Berlin", "Paris"))
print("\nEntre Oslo et Berne:")
print(path_duration_between_two_capitals("Oslo", "Berne"))
print("")

print("")
print("------------------")
print("Test de path_duration_list_of_capitals: \nCas ou le chemin entre en parametre est valide")
print(path_duration_list_of_capitals(["Berlin", "Paris", "Rome", "Athènes"]))
print("\nCas ou le chemin entre en parametre est invalide")
print(path_duration_list_of_capitals(["Berlin", "Paris", "Rome", "Athènes", "Paris"]))
print("\nAutre cas ou le chemin entre en parametre est valide")
print(path_duration_list_of_capitals(["Tallinn", "Helsinki", "Stockholm", "Riga", "Vilnius", "Varsovie", "Bratislava", "Prague", "Berlin", "Vienne", "Budapest", "Ljubljana", "Rome", "Athènes"]))
print("")
