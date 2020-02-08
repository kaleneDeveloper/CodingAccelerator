import os
import os.path

curent_path = "/home/kalene/Developer/Python/Udemy/Créer une structure de dossiers"


d = {"Films": ["Le seigneur des anneaux",
                "Harry Potter",
                "Moon",
                "Forrest Gump"],
    "Employes": ["Paul",
                "Pierre",
                "Marie"],
    "Exrcices": ["les_variabler",
                "les_fichier",
                "les_boucles"]}


# for key, value in d.items():
#     for sub in value:
#         os.makedirs(os.path.join(curent_path, key, sub),exist_ok=True)
       
    
for key in d.keys():
    for sub in d.get(key):
        os.makedirs(os.path.join(curent_path, key, sub),exist_ok=True)
