"""
Johann Touta
Youssef Takaya
Karine Collet
Margot Georget

Fichier contenant les fonctions prenant en compte les distances en km entre les capitales.

Ce fichier contient les fonctions suivantes :
1- une fonction qui prend en paramètre une capitale et qui retourne toutes ses capitales frontalières avec la
distance qui les sépare
2- une fonction qui prend en paramètre une capitale et qui retourne la capitale frontalière la plus proche en km
3- une fonction qui prend en paramètre une capitale et un entier n et qui retourne les capitales frontalières qui
se trouvent à moins de n km de distance
4- une fonction qui prend en paramètre une liste de capitales correspondant à une chaine existante dans le graphe
et qui retourne le nombre de km de ce trajet  

Les tests des fonctions 1 à 3 se trouvent dans le fichier "test_fonctions_distances". La fonction 4 est testée
dans le fichier ""test..." pour l'associer à une fonction retournant une chaine existante.

"""

###import librairies
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from outils_matrices import*

#import des données
voyages = pd.read_csv('capitales.csv',sep=";")

#construction et affichage graphe non orienté et à arêtes avec poids
G = nx.from_pandas_edgelist(voyages,source='DEPART',target='ARRIVEE', edge_attr='DISTANCES',create_using=nx.Graph())

def distances_capitales_frontalieres (capitale):
    """
    Données : capitale: pays faisant partie de notre liste de capitales 
    Rôle : Retourne toutes les capitales reliées directement à 'capitale' ainsi que la
    distances en km avec 'capitale'
    """
    d=dict()#création du dico qui contiendra nos capitales frontalières comme clé et leur distance les séparant de 'capitale' comme valeur 
    a = [*G.adj.get(capitale)] #création de la liste qui contient toutes les capitales frontalières 
    for i in range (len(a)): #boucle sur cette liste
        #pour chaque capitales de la liste on lui associe la distance la séparant de 'capitale' en récupérant la valeur de l'arête
        #qui les relie grace à la matrice d'adjacence du graphe G valué 
        d[a[i]]=nx.attr_matrix(G,edge_attr='DISTANCES')[0][nx.attr_matrix(G)[1].index(capitale),nx.attr_matrix(G)[1].index(a[i])]
    return d


def distances_min_capitales_frontalieres (capitale):
    """
    Données : capitale: pays faisant partie de notre liste de capitales 
    Rôle : Retourne la capitale reliée dirctement à 'capitale' ayant
    une distance minimale
    """
    d = distances_capitales_frontalieres (capitale) #créer  le dico des capitales frontalières avec leur distance 
    d_trie=sorted(d.items(), key=lambda x: x[1],reverse=False)#trie le dico en ordre croissant
    return d_trie[0][0]+": "+ str(d_trie[0][1]) #retourne le premier item du dico trié qui correspond
    #à la capitale ayant la plus petite distance 


def distances_inferieures_capitales_frontalieres (capitale, distance):
    """
    Données: capitale: pays faisant partie de notre liste de capitales
             distance: en km
    Rôle: Retourne toutes les capitales frontalièrs avec une distance
    inférieur ou égal à 'distance'
    """
    d =dict()#création du dico qui contiendra nos capitales frontalières avec une distance inférieur
    #ou égal à 'distance' comme clé et leur distance les séparant de 'capitale' comme valeur
    a = [*G.adj.get(capitale)]#création de la liste qui contient toutes les capitales frontalières
    for i in range (len(a)): #boucle sur cette liste 
        if nx.attr_matrix(G,edge_attr='DISTANCES')[0][nx.attr_matrix(G)[1].index(capitale),nx.attr_matrix(G)[1].index(a[i])] <= distance:
            #verifie que le poids de l'arête entre 'capitale' et la capitale a[i] est bien inferieur ou egal à 'distance'
            d[a[i]]=nx.attr_matrix(G,edge_attr='DISTANCES')[0][nx.attr_matrix(G)[1].index(capitale),nx.attr_matrix(G)[1].index(a[i])]
            #si oui on l'ajoute au dico
    if (len(d)==0): #si la liste est vide on previent qu'aucune capitale ne correspond à la demande 
        print("\nIl n'existe aucune capitale frontalière ayant une distance inférieure à",distance,"km pour cette capitale")
    return d


def distance_trajet(chaine):
    """
    Donnée: chemin : une liste de capitale correspondant à une chaine
    entre deux capitales
    Rôle : retourne la distance total parcouru en prenant cette chaine 
    """
    result=0 #initialise la variable result à 0
    for i in range (len(chaine)-1): #boucle sur les capitales de la chaine. On s'arrête à len(chaine)-1 car on ne s'intéresse qu'aux arêtes
        # entre les capitales qui se succèdent. Il n'y a pas de capitale après chaine[len(chaine) donc il n'y a pas d'arête.
        
        #ajoute à la variable result le poids de l'arête entre la capitale i et i+1 de la chaine 
        result+= nx.attr_matrix(G,edge_attr='DISTANCES')[0][nx.attr_matrix(G)[1].index(chaine[i]),nx.attr_matrix(G)[1].index(chaine[i+1])]
    return result    

