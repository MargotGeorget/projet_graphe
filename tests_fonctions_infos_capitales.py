from fonctions_infos_capitales import*
from fonctions_generales import*

#Création de nos capitales:
lis_capitale=infos_initialisation()


print("\nTest fonction affiche_capitale:")
print("\nTest avec Madrid:")
affiche_capitale(lis_capitale[index_capitale("Madrid")])

print("\nTest avec Paris:")
affiche_capitale(lis_capitale[index_capitale("Paris")])

print("\nTest avec Varsovie:")
affiche_capitale(lis_capitale[index_capitale("Varsovie")])

print("\nTest avec Helsinki:")
affiche_capitale(lis_capitale[index_capitale("Helsinki")])

print("\nTest fonction liste_capitale:")
print(liste_capitale())

print("\nTest fonction affiche_lis_capitale:")
print("Test avec [Berlin,Luxembourg,Paris]")
affiche_lis_capitale(["Berlin","Luxembourg","Paris"])
#test mise en situation
print("\nTest mise en situation:")
lis= plus_courte_distance("Oslo","Vienne")
print(lis)
affiche_lis_capitale(lis)


affiche_lis_capitale(['Oslo', 'Stockholm', 'Copenhague', 'Berlin', 'Berne'])
