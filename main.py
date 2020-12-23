import importlib
#TODO: USE IMPORTLIB IN ORDER TO ACTUALLY IMPORT THESE FOLDERS
SaveSets = importlib.import_module("Utilities.SaveSet")
Set = importlib.import_module("Utilities.Set")
DownloadSets = importlib.import_module("Utilities.DownloadSets")
import os
option = 15
while option != 4:

    option = int(input("Welcome to Mem-O-Rise\nA CMD powered memorizing tool\nPlease Choose An Option\n1) Use existing set\n2) Create new set\n3) Delete Set\n4) Exit Program\n"))

    if option == 1:
        name = input("What is the name of the set?\n")
        setFinder = DownloadSets.DownloadSets("C:\Code\Python\Mem-O-Rise\Data\Sets.txt")
        currentSet = setFinder.importSet(name)

    if option == 2:
        name = input("What is the new sets name?\n")
        newName = Set.Set(name)
        newName.initializeData()

    if option == 4:
        os._exit(0)
