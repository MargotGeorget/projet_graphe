"""
Johann Touta
Margot Georget
Youssef Tekaya
Karine Collet


Fichier représentant le 'logiciel' final, permet une interaction avec
l'utilisateur.
Permet de tester toutes les fonctions créées

"""


from fonctions_generales import*
from fonctions_distances import*
from fonctions_durees import*
from fonctions_infos_capitales import*
from fonctions_durees_visite import*

action_quitter = 0
action_menu_principal = 1
action_menu_informations_pays = 2
action_menu_capitales_frontalieres = 3
action_menu_chaines = 4
action_menu_distances = 5
action_menu_durees = 6
action_menu_generale = 7
action_menu_durees_visite = 8 


action = action_menu_principal
print("Bonjour! Bienvenue dans notre agence!"
      "\nVous revez de visiter les capitales Européennes mais "
      "vous ne savez pas encore comment organiser votre voyage?"
      "\nCe logiciel est fait pour vous! ")
while action != action_quitter:
    if action == action_menu_principal:
        print("\n------------------------------")
        print("0 : Quitter ")
        print("1 : Afficher des informations concernant les capitales")
        print("2 : Rechercher les capitales frontalières à une autre capitale")
        print("3 : Rechercher des trajets entre deux capitales")
        choix = input("Votre choix ? ")
        if choix == "0":
            action = action_quitter
        elif choix == "1":
            action = action_menu_informations_pays
        elif choix == "2":
            action = action_menu_capitales_frontalieres
        elif choix == "3":
            action = action_menu_chaines
        else:
            print("Choix incompris")
            
    elif action == action_menu_informations_pays :
        print("\n------------------------------")
        print("0 : Revenir au menu principal")
        print("1 : Afficher les informations complètes d'une capitale")
        print("2 : Recherches sur les durées de visite")
        choix = input("Votre choix ? ")
        if choix == "0":
            action = action_menu_principal
        elif choix == "1":
            capitale=choix_infos()
            action = action_menu_principal
        elif choix == "2":
            action = action_menu_durees_visite
        else:
            print("Choix incompris")

    elif action == action_menu_durees_visite :
        print("\n------------------------------")
        print("Les durées de visites sont comprises entre 2 et 7 jours")
        print("\n0 : Revenir au menu principal")
        print("1 : Afficher les capitales dont la durée de visite est inférieure à... ")
        print("2 : Afficher les capitales dont la durée de visite est égale à...")
        print("3 : Afficher les capitales dont la durée de visite est supérieure à...")
        print("4 : Afficher la durée de visite d'une capitale")
        choix = input("Votre choix ? ")
        if choix == "0":
            action = action_menu_principal
        elif choix == "1":
            duree = int(input("Entrez une durée en jours: "))
            print("\n",duree_visite_inferieur_a(duree))
            action = action_menu_durees_visite
        elif choix == "2":
            duree = int(input("Entrez une durée en jours: "))
            print("\n",duree_visite_egale_a(duree))
            action = action_menu_durees_visite
        elif choix == "3":
            duree = int(input("Entrez une durée en jours: "))
            print("\n",duree_visite_superieur_a(duree))
            action = action_menu_durees_visite
        elif choix == "4":
            capitale = choix_capitale()
            print("\n",duree_visite_capitale(capitale))
            action = action_menu_durees_visite
        else:
            print("Choix incompris")

        
    elif action == action_menu_capitales_frontalieres :
        print("\n------------------------------")
        print("0 : Revenir au menu principal")
        print("1 : Recherches générales")
        print("2 : Recherches en fonction des distances en kms entre les capitales ")
        print("3 : Recherches en fonction des durées en minutes entre les capitales")
        choix = input("Votre choix ? ")
        if choix == "0":
            action = action_menu_principal
        elif choix == "1":
            action = action_menu_generale
        elif choix == "2":
            action = action_menu_distances
        elif choix == "3":
            action = action_menu_durees
        else:
            print("Choix incompris")

    elif action == action_menu_generale :
        print("\n------------------------------")
        print("0 : Revenir au menu principal")
        print("1 : Afficher les capitales frontalières à une capitale")
        print("2 : Savoir si deux capitales sont frontalières ou non")
        
        choix = input("Votre choix ? ")
        if choix == "0":
            action = action_menu_principal
        elif choix == "1":
            capitale = choix_capitale()
            liste = capitales_frontalieres(capitale)
            print("\n",liste)
            print("\nVoulez vous connaitre les informations de ces capitales?")
            print("0 : Oui")
            print("1 : Non, revenir au menu principal")
            choix = input("Votre choix ? ")
            if choix == "0" :
                print("\n")
                affiche_lis_capitale(liste)
                action = action_menu_capitales_frontalieres 
            if choix == "1" :
                action = action_menu_capitales_frontalieres 
        elif choix == "2":
            capitale1 = choix_capitale()
            capitale2 = choix_capitale()
            if(is_capitales_frontalieres(capitale1,capitale2)):
                print("Les capitales sont frontalières")
            else:
                print("Les capitales ne sont pas frontalières")
            action = action_menu_capitales_frontalieres 
        else:
            print("\nChoix incompris")

    elif action == action_menu_distances :
        print("\n------------------------------")
        print("0 : Revenir au menu principal")
        print("1 : Afficher les capitales frontalières à une capitale et leurs distances")
        print("2 : Afficher la capitale frontalière la plus proche en kilomètres")
        print("3 : Afficher toutes les capitales frontalières ayant une distance infèrieure à une distance donnée")

        choix = input("Votre choix ? ")
        if choix == "0":
            action = action_menu_principal
        elif choix == "1":
            capitale = choix_capitale()
            print("\n",distances_capitales_frontalieres (capitale))
            action = action_menu_capitales_frontalieres 
        elif choix == "2":
            capitale = choix_capitale()
            print("\n",distances_min_capitales_frontalieres (capitale))
            action = action_menu_capitales_frontalieres
        elif choix == "3":
            capitale = choix_capitale()
            distance= int(input("Quelle distance?"))
            print("\n",distances_inferieures_capitales_frontalieres (capitale, distance))
            action = action_menu_capitales_frontalieres
        else:
            print("\nChoix incompris")

    elif action == action_menu_durees :
        print("\n------------------------------")
        print("0 : Revenir au menu principal")
        print("1 : Afficher les capitales frontalières à une capitale et leurs durees")
        print("2 : Afficher la capitale frontalière la plus proche en temps")
        print("3 : Afficher toutes les capitales frontalières ayant une durée infèrieure à une durée donnée")

        choix = input("Votre choix ? ")
        if choix == "0":
            action = action_menu_principal
        elif choix == "1":
            capitale = choix_capitale()
            print("\n",border_capitals(capitale))
            action = action_menu_capitales_frontalieres 
        elif choix == "2":
            capitale = choix_capitale()
            print("\n",nearest_border_capital(capitale))
            action = action_menu_capitales_frontalieres
        elif choix == "3":
            capitale = choix_capitale()
            duree= int(input("Quelle durée?"))
            result = accessible_capitals(capitale, duree)
            if (len(result)>0):
                print("\n",result)
            else :
                print("\nIl n'y pas de capitale correspondant à cette recherche")
            action = action_menu_capitales_frontalieres
        else:
            print("\nChoix incompris")
            
    elif action == action_menu_chaines :
        print("\n------------------------------")
        print("0 : Revenir au menu principal")
        print("1 : Afficher une chaîne de taille 2 entre deux capitales")
        print("2 : Afficher le plus court trajet entre deux capitales")
        choix = input("Votre choix ? ")
        if choix == "0":
            action = action_menu_principal
        elif choix == "1":
            capitale1 =  choix_capitale()
            capitale2 =  choix_capitale()
            chaine = chaine_longueur2(capitale1,capitale2)
            if (len(chaine)!=0):
                print("\n",chaine)
                print("\nLe trajet fait ",distance_trajet(chaine)," km et dure ",path_duration_list_of_capitals(chaine)," minutes")
                print("\nLe séjour dure", duree_sejour(chaine), "jours")
                        
                print("\n0 : Revenir au menu")
                print("1 : Afficher les informations des capitales du trajet")
                
                choix = input("Votre choix ? ")
                if choix == "0" :
                    action = action_menu_chaines
                elif choix == "1" :
                    print("\n")
                    affiche_lis_capitale(chaine)
                    action = action_menu_chaines
                else:
                    print("\nChoix incompris")
            action = action_menu_chaines
                
        elif choix == "2":
            capitale1 =  choix_capitale()
            capitale2 =  choix_capitale()
            chaine = plus_courte_distance(capitale1,capitale2)

            print("\n",chaine)
            print("\nLe trajet fait ",distance_trajet(chaine)," km et dure ",path_duration_list_of_capitals(chaine)," minutes")
            print("\nLe séjour dure", duree_sejour(chaine), "jours")

            print("\n0 : Revenir au menu")
            print("1 : Afficher les informations des capitales du trajet")
            
            choix = input("Votre choix ? ")
            if choix == "0" :
                action = action_menu_chaines
            elif choix == "1" :
                print("\n")
                affiche_lis_capitale(chaine)
                action = action_menu_chaines 
            else:
                print("\nChoix incompris")

    else:
        print("\nProblème! Action non prévue.")

print("\nMerci de votre visite !\nA bientôt")
