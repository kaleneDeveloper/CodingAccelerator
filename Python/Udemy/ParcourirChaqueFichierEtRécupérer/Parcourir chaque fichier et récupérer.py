import glob
import json
import os
curent_path = "/home/kalene/Developer/Python/Udemy/Parcourir chaque fichier et récupérer/**"

path_glob = glob.glob(curent_path, recursive=True)

number_of_acompte = None
number_social_security = None

# if Path('Parcourir chaque fichier et récupérer.py').is_file():
#     print ("File exist")
# else:
#     print ("File not exist")

for files in path_glob: # files is eagle at every files in the directories
	if files.endswith(".json"):
		with open(files, "r") as f:# open files and read the contents to store it in f
			data_json = json.load(f)
			if "Credit Mutuel" in data_json:
				number_of_acompte = data_json["Credit Mutuel"].get("Numero de compte","test")
	elif files.endswith(".txt"):
		with open(files, "r") as f:
			data_txt = f.read()
			if "Numéro de sécurité sociale" in data_txt:
				number_social_security = data_txt.split(":")[-1]

print(number_of_acompte)          
print(number_social_security)