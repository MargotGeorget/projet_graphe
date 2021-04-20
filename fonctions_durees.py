"""

Ce fichier répertorie un ensemble de fonctions permettant de travailler sur
les capitales, en fonction des durées d'accessibilites de ces dernieres.

- accessible_capitals(depart, duree) : Retourne toutes les capitales frontalière accessibles à celle entrée en paramètre en un temps inférieur ou égal a une durée renseignée en parametre.
- border_capitals(capitale) : Retourne toutes les capitales frontalères de celle entrée en paramètre ainsi que la durée d'accessibilté pour chacune d'entre elles.
- nearest_border_capital(capitale) : Retourne LA capitale frontalière la plus proche de celle entree en parametre, ainsi que le temps necessaire pour s'y rendre.
- exist_path_between_two_capitals(capitales1, capitales2) : Retourne un booléen en fonction de si oui ou non il existe un chemin direct entre deux capitales.
- path_duration_between_two_capitals(capitales1, capitales2) : Retourne la plus courte duree du chemin entre deux capitales entrées en paramètres.
- path_duration_list_of_capitals(list_of_capitals) : Retourne la duree de parcours du chemin formé d'une liste de capitales entrées en parametre.


"""


#Import des librairies
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Import des données
voyages = pd.read_csv('capitales.csv',sep=";")

#Construction et affichage des graphes non orienté et à arêtes avec poids

G2 = nx.from_pandas_edgelist(voyages,source='DEPART',target='ARRIVEE', edge_attr='Duree_en_minutes',create_using=nx.Graph())

pos = nx.spring_layout(G2)
edge_labels_list=nx.get_edge_attributes(G2,'Duree_en_minutes')

nx.draw_networkx(G2,pos,with_labels=True)
nx.draw_networkx_edge_labels(G2,pos,edge_labels=edge_labels_list)
##plt.show()




"------------------------------------------------------------"

def accessible_capitals(depart, duree):
    
    """
    Données: Une capitale de départ et une duree en minutes
    Resultat: Un dictionnaire ayant pour clés les capitales accessibles à partir de depart, et pour valeurs leur durees d'accessibilites depuis depart
    Rôle: Retourne toutes les capitales accessibles a partir de depart et dont la duree d'accessiblite est inferieure ou egale a la duree entree en parametre
    """
    
    d = dict() #Dictionnaire qui contiendra toutes les villes accessibles ainsi que la duree d'accessibilite par rapport a ville de départ
    liste = nx.attr_matrix(G2, edge_attr='Duree_en_minutes')[0][nx.attr_matrix(G2, edge_attr='Duree_en_minutes')[1].index(depart)] #G2 est un graphe ayant pour arêtes la durée en minutes et non la distances
    for i in range (G2.order()): 
        if(liste[0,i] <= duree and liste[0,i] != 0):
            d[nx.attr_matrix(G2, edge_attr='Duree_en_minutes')[1][i]] = liste[0,i]
    return d


"------------------------------------------------------------"

def border_capitals(capitale):

    """
    Données: Une capitale de l'espace Shengen
    Resultat: Un dictionnaire ayant pour clés les capitales frontalières au parametre "capitale", et pour valeurs leurs durees d'accessibilite (en minutes) depuis capitale.
    """

    result = dict()
    tab = nx.attr_matrix(G2, edge_attr='Duree_en_minutes')[0][nx.attr_matrix(G2)[1].index(capitale)]
    for i in range(G2.order()):
        if(tab[0,i] != 0):
            result[nx.attr_matrix(G2, edge_attr='Duree_en_minutes')[1][i]] = tab[0,i]
    return result


"------------------------------------------------------------"


def nearest_border_capital(capitale):

    """
    Données: Une capitale de l'espace Shengen
    Resultat: Chaine de caractere contenant LA capitale la plus proche et sa duree d'accessibilite (minutes) en partant de capitale.
    """
    
    result = dict()
    dictCapitals = border_capitals(capitale)    #Un dictionnaire contenant toutes les capitales frontalières et leurs durees d'accessibilite (minutes) en partant de capitale.
    tmp = sorted(dictCapitals.items(), key=lambda x : x[1], reverse = False)    #Trie du dictionnaire dictCapitals. IL DEVIENT UNE LISTE !
    result = (tmp[0][0] + " : " + str(tmp[0][1]) + " minutes.") #Recuperation du premier element de tmp et conversion en chaine de caractere
    return result


"------------------------------------------------------------"

def exist_path_between_two_capitals(capitales1, capitales2):

    """
    Données: Deux capitales quelconques de l'espace Shengen
    Resultat: Booleen : True si les deux capitales entrees en parametre sont frontalieres, False sinon
    """
    
    if( ( nx.attr_matrix(G2, edge_attr='Duree_en_minutes')[0][nx.attr_matrix(G2)[1].index(capitales1), nx.attr_matrix(G2)[1].index(capitales2)] ) != 0 ):
        return True
    return False


"------------------------------------------------------------"

def path_duration_between_two_capitals(capitales1, capitales2):
    
    """
    Données: Deux capitales quelconques de l'espace Shengen
    Resultat: Flottant : Duree d'accessibilite entre capitales1 et capitales2 si elles sont frontalieres, 0 si elles ne le sont pas
    """
    
    if(exist_path_between_two_capitals(capitales1, capitales2)):
        return nx.attr_matrix(G2, edge_attr='Duree_en_minutes')[0][nx.attr_matrix(G2)[1].index(capitales1), nx.attr_matrix(G2)[1].index(capitales2)]
    return 0


"------------------------------------------------------------"

def path_duration_list_of_capitals(list_of_capitals):

    """
    Données: Une liste de capitales de l'espace Shengen
    Resultat: Flottant : Duree du plus court chemin entre les capitales consecutives de la liste
    """
    
    duration = 0
    
    if(len(list_of_capitals) > 1):
        
        for i in range(0, len(list_of_capitals)-1, 1):
            
            if(exist_path_between_two_capitals(list_of_capitals[i], list_of_capitals[i+1])):
                
                duration = duration + path_duration_between_two_capitals(list_of_capitals[i], list_of_capitals[i+1])
                
            else:
                print("/!\ Trajet impossible car", list_of_capitals[i], "et", list_of_capitals[i+1], "ne sont pas frontalieres. Duree jusqu'a", list_of_capitals[i])
                
    elif(len(list_of_capitals) == 1):
        return duration
    else:
        return("Erreur. La liste entree est invalide.")
    
    return duration


"------------------------------------------------------------"


    

