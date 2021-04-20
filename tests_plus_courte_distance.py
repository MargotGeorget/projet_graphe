###import librairies
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from outils_matrices import*
from fonctions_generales import*
from fonctions_distances import*

print("Test fonction plus_courte_distance:")

print("\nTest de Berlin à Paris") 
print (plus_courte_distance("Berlin","Paris"))

print("\nTest de Varsovie à Riga") 
print (plus_courte_distance("Varsovie","Riga"))

print("\nTest de Varsovie à Vienne") 
print (plus_courte_distance("Varsovie","Vienne"))

print("\nTest de Paris à Budapest") 
print (plus_courte_distance("Paris","Budapest"))

print("\nTest de Helsinki à Rome") 
print (plus_courte_distance("Helsinki","Rome"))

print("\nTest de Lisbonne à Paris") 
print (plus_courte_distance("Lisbonne","Paris"))

print("\nTest de Oslo à Berlin") 
print (plus_courte_distance("Oslo","Berlin"))

print("\n\ntest distance trajet")
print("\nTest de Berlin à Paris") 
print(distance_trajet(plus_courte_distance("Berlin","Paris")))

print("\nTest de Varsovie à Riga") 
print(distance_trajet(plus_courte_distance("Varsovie","Riga")))

print("\nTest de Lisbonne à Paris") 
print(distance_trajet(plus_courte_distance("Lisbonne","Paris")))
