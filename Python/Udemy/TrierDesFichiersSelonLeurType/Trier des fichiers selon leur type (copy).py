from glob import glob
# import glob
import os
import shutil

directories_and_extensions = {
     "Music":(".wav",".mp3"),
     "Videos":(".mov",".mp4"),
     "Pictures":(".jpg",".jpeg",".png"),
     "Documents":(".pdf")
     }
current_directory = os.path.dirname(__file__)
current_files = glob(os.path.join(current_directory,"**"),recursive=True)

for directories_type, extensions in directories_and_extensions.items():
    os.makedirs(os.path.join(current_directory,directories_type),exist_ok=True)
    for extension in extensions:
        for fichier in current_files:
            if fichier.endswith(extension):
                shutil.move(fichier,os.path.join(current_directory,directories_type))
   
for fichier in current_files:
    if fichier.endswith(".json"):
        shutil.move(fichier,os.path.join(current_directory))
