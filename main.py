import numpy as np
import pandas as pd


classeA = pd.read_csv("data/classe_A.csv")
classeB = pd.read_csv("data/classe_B.csv")

print("Classe A: \n")
print(classeA.head())
print("Classe B: \n")
print(classeB.head())


classeA["sexe"] = classeA["sexe"].fillna("M")
classeB["sexe"] = classeB["sexe"].fillna("F")

print("Validation:\n")
print("Classe A: \n")
print(classeA.head())
print("Classe B: \n")
print(classeB.head())


#L'ajout des notes manquants
classeA["Projet"] = [15, 18, 12, 19, 11, 16, 13, 17, 10, 20, 15, 9, 17, 13, 18]
classeB["Projet"] = [14, 17, 11, 18, 10, 15, 12, 16, 11, 19, 14, 8, 16, 12, 17]
