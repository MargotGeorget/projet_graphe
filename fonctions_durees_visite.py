"""
Johann Touta
Youssef Takaya
Karine Collet
Margot Georget

Fichier contenant les fonctions prenant en compte les durées de visite des capitales 

Ce fichier contient les fonctions suivantes :
1- une fonction qui prend en paramètre un entier et qui retourne toutes les capitales ayant une durée de visite inférieur ou égale à l'entier 
2- une fonction qui prend en paramètre un entier et qui retourne toutes les capitales ayant une durée de visite égale à l'entier 
3- une fonction qui prend en paramètre un entier et qui retourne toutes les capitales ayant une durée de visite supérieur ou égale à l'entier 
4- une fonction qui prend en paramètre une liste de capiatles et qui retourne la durée de séjour total pour visiter les capitales de la liste
5- une fonction qui prend en paramètre une capitale et qui retourne la duree de visite de cette capitale

Les tests des fonctions 1 à 5 se trouvent dans le fichier "test_fonctions_durees_visite". 

"""

###import librairies
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from outils_matrices import*
from fonctions_infos_capitales import*

#import des données
voyages = pd.read_csv('capitales.csv',sep=";")

#construction et affichage graphe non orienté et à arêtes avec poids
G = nx.from_pandas_edgelist(voyages,source='DEPART',target='ARRIVEE',create_using=nx.Graph())

liste_capitales = infos_initialisation()

#Initialisation de l'attribut Duree_visite pour chaque capitale du graphe à partir
#de notre liste de Capitale (géré dans le fichier fonction_infos_capitale)
for capitale in liste_capitales :
    G.nodes[capitale.capitale]['Duree_visite']=int(capitale.temps)


def duree_visite_inferieur_a (entier):
    """
    Donnée: entier : un entier
    Rôle : retourne un dictionnaire contenant toute les capitales ayant un
    durée de visite inférieur ou égal à 'entier'
    """
    d = dict()
    for i in G :
        if (G.nodes[i]['Duree_visite']<=entier):
            d[i]=G.nodes[i]['Duree_visite']
    return d

def duree_visite_egale_a (entier):
    """
    Donnée: entier : un entier
    Rôle : retourne un dictionnaire contenant toute les capitales ayant un
    durée de visite égale à 'entier'
    """
    d = dict()
    for i in G :
        if (G.nodes[i]['Duree_visite']==entier):
            d[i]=G.nodes[i]['Duree_visite']
    return d

def duree_visite_superieur_a (entier):
    """
    Donnée: entier : un entier
    Rôle : retourne un dictionnaire contenant toute les capitales ayant un
    durée de visite supérieur ou égale à 'entier'
    """
    d = dict()
    for i in G :
        if (G.nodes[i]['Duree_visite']>=entier):
            d[i]=G.nodes[i]['Duree_visite']
    return d

def duree_sejour(liste):
    """
    Données : liste : une liste de capitale 
    Rôle : retourne la somme des durées de visite pour chaque capitales de la liste 
    """
    result = 0
    for i in range (len(liste)):
        result+=G.nodes[liste[i]]['Duree_visite']
    return result

def duree_visite_capitale(capitale):
    """
    Donnée : capitale : une capitale de notre liste
    Rôle : retourne la duree de visite de la capitale
    """
    return G.nodes[capitale]['Duree_visite']
