import os
import json

while True:
    _list = input("Take your list or create new list: ")
    if not _list:
        print("Insert text.")
    elif _list.endswith(".json"): # if the file json exist
        print(f"{_list} selected.")
        break
    elif os.path.isfile(_list): # if the file is not a list .json
        with open(_list, 'r') as f:
            file = f.read().splitlines()
        print(f"{_list} selected.")
        os.rename(_list, _list + ".json")
        with open(_list + ".json", "w") as f:
            json.dump(list(file), f, indent = 4) 
        print(f"{_list}.json created and has been updated.")
        _list = _list + ".json"
        break
    else: os.mknod(_list + ".json")
    with open(_list + ".json", "w") as f:
        json.dump([], f) 
    print(f"{_list} create.")
    _list = _list + ".json"
    break

dossier_courant = os.path.dirname(__file__)
chemin_liste = os.path.join(dossier_courant, _list)

if os.path.exists(chemin_liste):
    with open(chemin_liste, "r") as f:
        liste_de_courses = json.load(f)
else:
    liste_de_courses = []

affichage = """
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Terminer
"""

option = "0"

while option != "5":
    option = input(affichage)
    if option == "1":
        item_a_ajouter = input("Entrez le nom de l'élément à ajouter: ")
        liste_de_courses.append(item_a_ajouter)
    elif option == "2":
        item_a_retirer = input("Entrez le nom de l'élément à enlever: ")
        if item_a_retirer in liste_de_courses:
            liste_de_courses.remove(item_a_retirer)
    elif option == "3":
        if liste_de_courses:
            print("\n".join(liste_de_courses))
        else:
            print("La liste ne contient aucun élément.")
    elif option == "4":
        liste_de_courses.clear()

with open(chemin_liste, "w") as f:
    json.dump(list(liste_de_courses), f, indent = 4)