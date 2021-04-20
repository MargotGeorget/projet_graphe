###import
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from outils_matrices import*
#from projet_capitales import*

#import des données
voyages = pd.read_csv('capitales.csv',sep=";")

#construction et affichage graphe non orienté et à arêtes avec poids
G = nx.from_pandas_edgelist(voyages,source='DEPART',target='ARRIVEE', edge_attr='DISTANCES',create_using=nx.Graph())

print("\nTEST PRODUIT MATRICE")
M=nx.attr_matrix(G)[0]
M=produit_matrices1(nx.attr_matrix(G)[0],nx.attr_matrix(G)[0])
print(M)

print("\nchemin taille 2 Berlin, Oslo")
print(M[nx.attr_matrix(G)[1].index("Berlin")][nx.attr_matrix(G)[1].index("Oslo")])
print("\nchemin taille 2 Paris, Lisbonne")
print(M[nx.attr_matrix(G)[1].index("Paris")][nx.attr_matrix(G)[1].index("Lisbonne")])
print("\nchemin taille 2 Madrid, Berlin")
print(M[nx.attr_matrix(G)[1].index("Madrid")][nx.attr_matrix(G)[1].index("Berlin")])

print("\nchemin taille 2 Varsovie, Vienne")
print(M[nx.attr_matrix(G)[1].index("Varsovie")][nx.attr_matrix(G)[1].index("Vienne")])

print(nx.attr_matrix(G)[1])

V=puissance_matrice_adjacence(nx.attr_matrix(G)[0],3)
print(V)

print("\nchemin taille 3 Berlin, Oslo")
print(V[nx.attr_matrix(G)[1].index("Berlin")][nx.attr_matrix(G)[1].index("Oslo")])
print("\nchemin taille 3 Paris, Lisbonne")
print(V[nx.attr_matrix(G)[1].index("Paris")][nx.attr_matrix(G)[1].index("Lisbonne")])
print("\nchemin taille 3 Madrid, Berlin")
print(V[nx.attr_matrix(G)[1].index("Madrid")][nx.attr_matrix(G)[1].index("Berlin")])

print("\nchemin taille 3 Varsovie, Vienne")
print(V[nx.attr_matrix(G)[1].index("Varsovie")][nx.attr_matrix(G)[1].index("Vienne")])
