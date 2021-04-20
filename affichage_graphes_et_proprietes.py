###import librairies
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#import des données
voyages = pd.read_csv('capitales.csv',sep=";")

#construction et affichage graphe non orienté et à arêtes avec poids : selon distances
G = nx.from_pandas_edgelist(voyages,source='DEPART',target='ARRIVEE', edge_attr='DISTANCES',create_using=nx.Graph())

pos = nx.spring_layout(G)
edge_labels_list=nx.get_edge_attributes(G,'DISTANCES')

nx.draw_networkx(G,pos,with_labels=True)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels_list)
plt.show()

#propriétés principales
print("nombre de sommets:",G.order())
print("nombre d'aretes:",G.size())
print(nx.info(G))
#densité (= nombre d'arêtes / nombre total d'arêtes ; boucles exclues)
print("densité:",nx.density(G))
#liste d'adjacence
print("liste adjacence")
Ladj=G.adj
#matrice d'adjacence
print("matrice adjacence")
print(nx.attr_matrix(G))

#construction et affichage graphe non orienté et à arêtes avec poids : selon temps
G = nx.from_pandas_edgelist(voyages,source='DEPART',target='ARRIVEE', edge_attr='Duree_en_minutes',create_using=nx.Graph())

pos = nx.spring_layout(G)
edge_labels_list=nx.get_edge_attributes(G,'Duree_en_minutes')

nx.draw_networkx(G,pos,with_labels=True)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels_list)
plt.show()

#propriétés principales
print("nombre de sommets:",G.order())
print("nombre d'aretes:",G.size())
print(nx.info(G))
#densité (= nombre d'arêtes / nombre total d'arêtes ; boucles exclues)
print("densité:",nx.density(G))
#liste d'adjacence
print("liste adjacence")
Ladj=G.adj
#matrice d'adjacence
print("matrice adjacence")
print(nx.attr_matrix(G))
