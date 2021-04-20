"""
Johann Touta
Youssef Tekaya
Karine Collet
Margot Georget

Fichier permettant de gérer les informations sur les capitales.

Ce fichier contient :
1- La déclaration de l'object Capitale
Dans ce fichier Capitale avec une majuscule fait référence à l'object, sans majuscule il s'agis simplement d'une chaine de cractère!!
2- Une fonction qui permet d'initialiser une liste de Capitale à partir d'un fichier csv
3- Une fonction qui initialise une liste de Capitale à partir de notre fichier csv "infos_capitales.csv"
4- Une fonction qui prend en paremètre une Capitale et qui affiche ses attributs
5- Une fonction qui prend en paramètre une liste de Capitale et qui affiche les attributs de chaque Capitales de la liste
6- une fonction qui retourne une liste contenant l'attributs capitales de toutes les Capitales de notre liste
7- Une fonction qui retourne l'index dans la liste de Capitale d'une capitale donnée
8- Une fonction qui permet à l'utilisateur de choisir une Capitale parmi la liste et retourne les infos de cette Capitale 
9- Une fonction qui permet de choisir une Capitale parmis la liste des Capitales et qui retourne l'attribut capitale de cette Capitale
10- une fonction qui prend en paramètre une liste de capitale et qui retourne la somme de leur durée de séjour 

"""

import csv

class Capitale(object):
    """
    Définition du type de données Capitale, contenant les capitales, leur pays,
    leur superficie en km2, le nombre d'habitants en millions et la durée
    estimée du temps de visite en jours.
    """
    def __init__( self,
                  valeur_capitale,
                  valeur_pays,
                  valeur_superficie,
                  valeur_habitants,
                  valeur_temps
                  ):
        self.capitale = valeur_capitale
        self.pays = valeur_pays
        self.superficie = valeur_superficie
        self.habitants = valeur_habitants
        self.temps = valeur_temps

def lecture_dans_fichier(nom_fichier):
    """
    Données : nom_fichier : chaîne de caractères
    Rôle : le fichier dont le nom est fourni en paramètre est supposé être
    un fichier au format csv avec des ; comme séparateur.
    Chaque ligne du fichier contient les valeurs de l'objet Capitale.
    La fonction lit le fichier et retourne l'information contenue
    sous forme d'une liste de type Capitale.
    """
    fichier = open(nom_fichier,"r",encoding="latin_1")
    cr = csv.reader(fichier,delimiter=";")
    cap = []
    for ligne in cr:
        capitale = ligne[0]
        pays = ligne[1]
        superficie = ligne[2]
        habitants = ligne[3]
        temps = ligne[4]
        c = Capitale(pays, capitale, superficie, habitants, temps)
        cap.append(c)
    fichier.close()
    return cap

def infos_initialisation():
    """
    Résultat : fichier infos_capitales.csv
    Rôle : configure et lit le fichier csv
    """
    return lecture_dans_fichier("infos_capitales.csv")

#Création de nos capitales 
lis_capitale=infos_initialisation()

def affiche_capitale(capitale):
    """
    Donnée : capitale : instance de type Capitale
    Rôle : affiche l'instance d'enregistrement de type Capitale
    """
    print("\nPays :",capitale.pays,
          "\nCapitale:",capitale.capitale,
          "\nSuperficie:",capitale.superficie,"km2",
          "\nNombre d'habitants:",capitale.habitants, "millions",
          "\nDurée de séjour:", capitale.temps, "jours")

def affiche_lis_objet_capitale(liste_capitale):
    """
    Donnée : liste_capitale : liste de valeurs de type Capitale
    Rôle : affiche les infos de toutes les capitales de la liste liste_capitale
    """
    lis=[]
    for i in range(0,len(liste_capitale),1):
        affiche_capitale(liste_capitale[i])

def affiche_lis_capitale(liste):
    """
    Donnée : liste : liste de chaine de caractère correspondant à des capitales
    Rôle : affiche les informations de ces capitales"""
    for i in range (len(liste)):
        a = index_capitale(liste[i])
        affiche_capitale(lis_capitale[a])


def liste_capitale():
    """
    Rôle : retourne la liste de l'attribut capitale des Capitales contenues dans
           notre liste de Capitales
    """
    lis=[]
    for i in range(0,len(lis_capitale),1):
        c=lis_capitale[i].capitale
        lis.append(c)
    return lis


def index_capitale (capitale):
    """
    Données : capitale: une chaine de caractère faisant référence à l'une de nos capitales
    Attention ici il ne s'agis pas de l'object Capitale mais uniquement d'une chaine de caractère
    Rôle: retourne la place de 'capitale' dans la liste de capitale (index)
    """
    lis=liste_capitale()
    a=lis.index(capitale)
    return a

def choix_infos():
    """
    Rôle : demande à l'utilisateur pour quelle capitale il souhaite voir
    les informations.
    """
    print("\nDe quelle capitale souhaitez-vous voir les informations ?"
      "\n0 : Berlin",
      "\n1 : Vienne",
      "\n2 : Bruxelles",
      "\n3 : Copenhague",
      "\n4 : Madrid",
      "\n5 : Tallinn",
      "\n6 : Helsinki",
      "\n7 : Paris",
      "\n8 : Athènes",
      "\n9 : Budapest",
      "\n10 : Rome",
      "\n11 : Riga",
      "\n12 : Vilnius",
      "\n13 : Luxembourg",
      "\n14 : Amsterdam",
      "\n15 : Varsovie",
      "\n16 : Lisbonne",
      "\n17 : Prague",
      "\n18 : Bratislava",
      "\n19 : Ljubljana",
      "\n20 : Stockholm",
      "\n21 : Berne",
      "\n22 : Vaduz",
      "\n23 : Oslo")
    try:
        info = int(input("\nJe vous écoute (seuls entiers acceptés)\n"))
        if (0 <= info <= 23):
            affiche_capitale(lis_capitale[info])
        else :
            print("\nVotre demande n'est pas possible.")
            choix_infos(lis_capitale)
    except TypeError as err:
        print("\nVotre demande n'est pas possible.")
        choix_infos(lis_capitale)
        raise

#choix_infos()
        
def choix_capitale():
    """
    Rôle : demande à l'utilisateur de choisir une Capitale et retourne l'attribut capitale
    de la Capitale choisie
    """
    print("\nChoisissez la capitale:"
      "\n0 : Berlin",
      "\n1 : Vienne",
      "\n2 : Bruxelles",
      "\n3 : Copenhague",
      "\n4 : Madrid",
      "\n5 : Tallinn",
      "\n6 : Helsinki",
      "\n7 : Paris",
      "\n8 : Athènes",
      "\n9 : Budapest",
      "\n10 : Rome",
      "\n11 : Riga",
      "\n12 : Vilnius",
      "\n13 : Luxembourg",
      "\n14 : Amsterdam",
      "\n15 : Varsovie",
      "\n16 : Lisbonne",
      "\n17 : Prague",
      "\n18 : Bratislava",
      "\n19 : Ljubljana",
      "\n20 : Stockholm",
      "\n21 : Berne",
      "\n22 : Vaduz",
      "\n23 : Oslo")
    info = int(input("\nJe vous écoute (seuls entiers acceptés):\n"))
    if (0 <= info <= 23):
        return lis_capitale[info].capitale
    else :
        print("\nVotre demande n'est pas possible.")
        choix_capitale()

