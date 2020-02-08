import logging
import json
import os

from constants import data_directory
# logging.basicConfig(level=logging.DEBUG,
#                     filename="app.log",
#                     filemode="w",
#                     format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.DEBUG)

# while True:
#     _list = input("Take your list or create new list: ")
#     if _list == "q" or _list == "Q":
#         exit(0)
#     if _list.endswith(".json"): # if the file json exist
#         print(f"{_list} selected.")
#         path = os.path.join(data_directory, _list)
#         with open(path, "r") as data:
#             json = json.load(data)
        
#         oldext = os.path.splitext(_list)[0]
#         _list = oldext
#         break
#     try:
#         with open(_list, "r") as f:
#             print(f"{_list} selected.")
#     except FileNotFoundError:
#         print("Wrong file or file path")
#     except UnicodeDecodeError:
#         print(f"Impossible open to file {file}")

    # if os.path.isfile(_list): # if the file is not a list .json
    #     with open(_list, 'r') as f:
    #         file = f.read()
    #     print(f"{_list} selected.")
    #     os.rename(_list, _list + ".json")
    #     with open(_list + ".json", "w") as f:
    #         json.dump(list(file), f, indent = 4) 
    #     print(f"{_list}.json created and has been updated.")
    #     _list = _list + ".json"
    #     break
    # else: os.mknod(_list + ".json")
    # with open(_list + ".json", "w") as f:
    #     json.dump([], f) 
    # print(f"{_list} create.")
    # _list = _list + ".json"
    # break


class List(list):
    def __init__(self, nom):
        self.nom = nom
    def add(self, element):
        if not isinstance(element, str):
            raise ValueError("Insert pls character string")
        if element in self:
            logging.debug(f"{element} is already in list.")
            return False
        self.append(element)
        return True
    
    def delele(self, element):
        if not element in self:
            logging.error(f"{element} no exist")
            return False
        if element in self:
            self.remove(element)
            return True
        return False
    def show(self):
        print(f"List {self.nom}")
        for element in self:
            print(f" - {element}")
    def save(self):
        path = os.path.join(data_directory, f"{self.nom}.json")
        try:
            if not os.path.exists(data_directory):
                os.makedirs(data_directory)
            with open(path, "w") as f: # create file.json in path
                json.dump(self, f, indent=4)
            return True
        except FileNotFoundError:
            print("Wrong file or file path")
            return False
        except UnicodeDecodeError:
            print(f"Impossible open to file {path}")
            return False

if __name__ == "__main__":
    list_ = List("Sopping list")
    list_.add("json")
    list_.show()
    list_.save()
    # resulat = list_.add(element)
    # if resultat:
    #     #add in graphic interface