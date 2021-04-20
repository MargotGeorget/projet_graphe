"""
Margot Georget
Johann Touta
Youssef Takaya
Karine Collet


Fichier contenant les fonctions générales, c'est à dire ne traitant pas des
poids des arêtes.

Ce fichier contient les fonctions suivantes :
1- Une fonction qui prend en paramètre une capitale et qui retourne toutes ses capitales frontalières
2- Une fonction qui prend en paramètre deux capitales et qui retourne si oui ou non ces deux capitales sont frontalières
3- Une fonction qui prend en paramètre deux capitales et un entier n et qui retourne le nombre de chaines de taille n
existant entre ces deux capitales
4- Une fonction qui prend en paramètre deux capitales et qui retourne, si elle existe, une chaine de longueur 2 entre
ces deux capitales
5- Une fonction qui prend en paramètre deux capitales et qui retourne la chaine passant par le moins de capitales possible
pour relier ces deux capitales

Les tests des fonctions 1 à 4 se trouvent dans le fichier "test_fonctions_generales". Pour la fonction 5 il y a un fichier
spécial de tests : "test_plus_courte_distance".

"""

###import librairies
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from outils_matrices import*

#import des données
voyages = pd.read_csv('capitales.csv',sep=";")

#construction et affichage graphe non orienté et non valué
G = nx.from_pandas_edgelist(voyages,source='DEPART',target='ARRIVEE',create_using=nx.Graph())

def capitales_frontalieres (capitale):
    """
    Données : capitale: ville faisant partie de notre liste de capitales 
    Rôle : Retourne toutes les capitales reliées directement à 'capitale'
    """
    return [*G.adj.get(capitale)] #retourne la liste d'adjacence correspondant à la capitale choisie


def is_capitales_frontalieres(depart,arrivee):
    """
    Données: depart/arrivee : ville faisant partie de notre liste de capitales
    Rôle: retourne True si les deux capitales sont frontalières, retourne False sinon
    """
    if (nx.attr_matrix(G)[0][nx.attr_matrix(G)[1].index(depart),nx.attr_matrix(G)[1].index(arrivee)]==0):
    #verifie si la matrice d'adjacence contient un 0 aux index correspondants aux capitales depart et arrivee
        result = False
    else:
        result = True
    return result


def nb_chaine_longueur_donnée (depart, arrivee, longueur):
    """
    Donées : depart/arrivee : deux capitales de notre liste
             longueur : un entier
    Rôle: Retourne le nombre de chaine de taille 'longueur' entre les capitales depart et arrivee
    """
    M=puissance_matrice_adjacence(nx.attr_matrix(G)[0],longueur)
    result = M[nx.attr_matrix(G)[1].index(depart)][nx.attr_matrix(G)[1].index(arrivee)]
    return "Il y a ",result, "chaine de taille ",longueur,"entre ",depart," et ",arrivee


def chaine_longueur2 (depart,arrivee):
    """
    Données: depart/arrivee : ville faisant partie de notre liste de capitales
    Rôle: Retourne aléatoirement, si elle existe, une chaine de longueur 2 entre les deux capitales
    (passant part 2 arcs)
    """
    result =[] #création de la liste qui contiendra les capitales correspondantes à notre chemin
    tmp =[] #variable tampon qui contient notre chemin, si le chemin n'exsite pas, permet de garder result vide 
    trouve = False #création d'un drapeau 
    tmp.append(depart)#le chaine commence forcément par notre capitale de depart 
    i=0
    while (i<len(G.adj.get(depart)) and not trouve): 
        j=0
        while (j<len(G.adj.get([*G.adj.get(depart)][i])) and not trouve):
        #boucle sur les capitales adjacentes a la capitale '[*G.adj.get(depart)][i]' correspondant à une capitale
        #adjacente a notre capitale de depart 
            if [*G.adj.get([*G.adj.get(depart)][i])][j]==arrivee:
                #si notre capitale d'arrivee fait partie des capitales adjacentes à la capitale que
                #l'on traite alors la chaine est trouvée
                tmp.append([*G.adj.get(depart)][i])
                trouve= True #permet de sortir de la boucle 
            j=j+1
        i=i+1
    tmp.append(arrivee)#notre chaine doit se terminer par la capitale d'arrivee
    if (not trouve) :
        print("Il n'y as pas de chaine de longueur 2 entre",depart, "et", arrivee)
    else :
        result = tmp
    return result


def plus_courte_distance (depart,arrivee):
    """
    Données: depart/arrivee: capitales faisant parties de notre liste  
    Rôle: retourne la plus courte distance entre les deux capitales (le plus
    petit nombre de capitales à traverser)
    """
    if (is_capitales_frontalieres(depart,arrivee)): #vérifie que les capitales ne sont pas frontalières
        return [depart,arrivee] #si c'est le cas retourne la chaine : depart, arrivee

    #sinon on initialise les variables 
    Ladj = G.adj #liste d'adjacence du graphe 
    trouve = False #création d'un drapeau 
    liste_futur = [] #liste des futurs capitales à vérifier 
    liste=[*Ladj.get(depart)] #liste de départ des sommets à vérifier : sommets adjacents au sommet de départ 
    cap_verifiee=dict() #dictionnaire qui associera à toutes les capitales vérifiés la capitale qui la précède
    
    for i in range (len(liste)): #boucle sur toutes les capitales adjacentes au sommet de depart 
        cap_verifiee[liste[i]]=depart #associe à chacune de ces capitales le sommet de départ comme prédecesseur
        
    while (len(cap_verifiee)<G.order() and not trouve): #boucle tant que toutes les capitales du graphe n'ont pas été
        #vérifiées ou que la chaine n'est pas trouvée
        i=0
        
        while (i<len(liste) and not trouve):#boucle sur la liste des capitales à vérifier
            if (is_capitales_frontalieres(liste[i],arrivee)): #vérifie si la capitale sur laquelle on travaille est frontalière
                #à notre capitale d'arrivee 
                cap_verifiee[arrivee]=liste[i]#la capitale sur laquelle on travaille est le predecesseur d'arrivee
                trouve= True #la chaine est trouvée alors on sort de la boucle
                
            else : #si la capitale n'est pas frontalière avec notre arrivee
                for k in range (len([*Ladj.get(liste[i])])): #on ajoute toutes les capitales frontalières à la capitale courante
                    #dans la liste des capitales qui seront à vérifier 
                    liste_futur.append([*Ladj.get(liste[i])][k])
                    if (not([*Ladj.get(liste[i])][k] in cap_verifiee)): #on indique à toutes les capitales frontalières a notre
                        #capitale courante qui ne sont pas deja dans le dico que notre capitale courante est leur prédécesseur
                        cap_verifiee[[*Ladj.get(liste[i])][k]]=liste[i]           
                            
            i+=1
        liste=liste_futur

    #retrouver le chemin le plus court
    ok = False #création d'un drapeu 
    result = [arrivee] #initialise la liste qui sera le chemin le plus court : permière capitale du chemin = capitale d'arrivee 
    a = arrivee 
    while (not ok):
        result.append(cap_verifiee.get(a))#on ajoute le predecesseur à notre chaine 
        a = cap_verifiee.get(a)
        if (cap_verifiee.get(a)==depart): # on s'arrête lorsqu'on est arrivé à notre sommet de départ 
            ok = True
            result.append(depart)#ajoute le dernier sommet

    #inverse le sens du chemin pour avoir un chemin depart -->arrivee et non arrivee-->départ 
    result.reverse()
    
    return result
