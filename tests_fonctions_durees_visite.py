###import librairies
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from outils_matrices import*
from fonctions_infos_capitales import*
from fonctions_durees_visite import*

print("Test fonction duree_visite_inferieur_a:")
print("Test avec entier = 2:")
print(duree_visite_inferieur_a(2))
print("\nTest avec entier = 5:")
print(duree_visite_inferieur_a(5))

print("____________________________________________________")

print("\nTest fonction duree_visite_egale_a:")
print("Test avec entier = 2:")
print(duree_visite_egale_a(2))
print("\nTest avec entier = 6:")
print(duree_visite_egale_a(6))

print("____________________________________________________")

print("\nTest fonction duree_visite_superieur_a:")
print("Test avec entier = 2:")
print(duree_visite_superieur_a(2))
print("\nTest avec entier = 5:")
print(duree_visite_superieur_a(5))

print("____________________________________________________")

print("\nTest fonction duree_sejour:")
print("Test avec [Berlin,Paris,Madrid]")
print(duree_sejour(['Berlin','Paris','Madrid']))
print("\nTest avec [Lisbonne,Madrid]")
print(duree_sejour(['Lisbonne','Madrid']))

print("____________________________________________________")

print("\nTest fonction duree_visite_capitale:")
print("Test avec Berlin")
print(duree_visite_capitale('Berlin'))
print("\nTest avec Oslo")
print(duree_visite_capitale('Oslo'))
