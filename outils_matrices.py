"""
Johann Touta
Youssef Takaya
Karine Collet
Margot Georget

Fichier contenant des fonctions permettant de travailler sur des matrices 

Ce fichier contient les fonctions suivantes :
1- une fonction qui prend en paramètre une matrice d'adjacence et qui calcule le carré de cette matrice 
2- une fonction qui prend en paramètre deux matrice d'adjacence et qui calcule le produit de ces deux matrices
3- une fonction qui prend en paramètre une matrice d'adjacence et une autre matrice et qui calcule le produit de ces deux matrices
4- une fonction qui prend en paramètre une matrice d'adjacence et un entier n et qui calcul la matrice à la puissance n

Les tests des fonctions se trouvent dans le fichier "test_outils_matrices".

Ce fichier à pour but d'utiliser la propriété suivante :
Propriété de l'itérée
Si A est la matrice d'adjacence d'un graphe fini G dont les sommets sont numérotés de 1 à n,
le nombre de parcours de longueur exactement k allant de i à j est le coefficient en position
(i, j) de la matrice A puissance k

"""

###import librairies
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def puissance2_matrice_adjacence (M):
    """
    Données: M : matrice d'adjacence
    Rôle: calcul M puissance 2
    """
    result=[]
    n=0
    for i in range (len(M)):
        l=[]
        for j in range (len(M)):
            n=0
            for k in range (len(M)):
                n+=M[k,j]*M[i,k]
            l.append(n)
        result.append(l) 
    return result

def produit_matrices1 (M1,M2):
    """
    Données: M1/M2 : matrices d'adjacences
    Rôle: calcul le produit de M1 et M2
    """
    result=[]
    n=0
    for i in range (len(M1)):
        l=[]
        for j in range (len(M1)):
            n=0
            for k in range (len(M1)):
                n+=M1[k,j]*M2[i,k]
            l.append(n)
        result.append(l) 
    return result

def produit_matrices2 (M1,M2):
    """
    Données: M1 : une matrice d'adjacence
             M2 : une matrice 
    Rôle: calcul le produit de M1 et M2
    Nuance avec produit_matrices1: pour acceder à l'élément (i,j) d'une matrice d'adjacence
    il faut utiliser M[i,j] alors que pour une matrice (liste de liste) il faut utiliser M[i][j]
    """
    result=[]
    n=0
    for i in range (len(M1)):
        l=[]
        for j in range (len(M1)):
            n=0
            for k in range (len(M1)):
                n+=M1[k,j]*M2[i][k]
            l.append(n)
        result.append(l) 
    return result

def puissance_matrice_adjacence (M,n):
    """
    Données: M : une matrice d'adjacence
             n : un entier 
    Rôle: calcul M puissance n
    """
    tmp=produit_matrices1(M,M)#utilise produit_matrices1 car M est un matrice d'adjacence
    #mais le calcul retourne une matrice (liste de liste) 
    for i in range (n-2):
        tmp=produit_matrices2(M,tmp)#utilise produit_matrices2 puisque tmp est une matrice (liste de liste)
    return tmp
