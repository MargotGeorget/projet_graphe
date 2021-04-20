###import
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from outils_matrices import*
from fonctions_generales import*

print("Test fonction capitales_frontalières:")
   
print("\nTest avec la capitale Madrid:")
print(capitales_frontalieres ("Madrid"))

print("\nTest avec la capitale Oslo:")
print(capitales_frontalieres ("Oslo"))

print("\nTest avec la capitale Berlin:")
print(capitales_frontalieres ("Berlin"))

print("_________________________________________________________")
print("Test fonction is_capitales_frontalières:")

print("\nTest avec Berlin et Paris:") 
print (is_capitales_frontalieres("Berlin","Paris"))

print("\nTest avec Berlin et Madrid:") 
print (is_capitales_frontalieres("Berlin","Madrid"))

print("\nTest avec Madrid et Lisbonne:") 
print (is_capitales_frontalieres("Madrid","Lisbonne"))


print("_________________________________________________________")
print("Test fonction nb_chaine_longueur_donnée:")

print("\nTest avec Vienne, Varsovie, longueur 3:")
print(nb_chaine_longueur_donnée ("Vienne", "Varsovie", 3))

print("\nTest avec Madrid, Berlin, longueur 5:")
print(nb_chaine_longueur_donnée ("Madrid", "Berlin", 5))

print("\nTest avec Varsovie, Vienne, longueur 2:")
print(nb_chaine_longueur_donnée ("Vienne", "Varsovie", 2))

print("\nTest avec Oslo, Londres, longueur 2:")
print(nb_chaine_longueur_donnée ("Oslo", "Lisbonne", 2))

       
print("_________________________________________________________")
print("Test fonction chaine_longueur2:")

print("\nTest avec Berlin et Paris:")
print (chaine_longueur2("Berlin","Paris"))

print("\nTest avec Varsovie et Vienne:")
print (chaine_longueur2("Varsovie","Vienne"))

print("\nTest avec Lisbonne et Paris:")
print (chaine_longueur2("Lisbonne","Paris"))

print("\nTest avec Oslo et Londres:")
print (chaine_longueur2("Oslo","Lisbonne"))
