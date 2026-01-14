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


#Calcule des Moyenne Finale
for df in [classeA, classeB]:
    df["Moyenne_DS"] = df[["DS1","DS2","DS3"]].mean(axis=1)
    df["Moyenne_finale"] = df["Moyenne_DS"] * 0.75 + df["Projet"] * 0.25

#َAffichage des résultats
print("Classe A: \n", classeA[["nom","Moyenne_DS","Projet","Moyenne_finale"]])
print("\nClasse B: \n", classeB[["nom","Moyenne_DS","Projet","Moyenne_finale"]])



#Meilleur Classe
classe_better = "Classe A" if classeA["Moyenne_finale"].mean() > classeB["Moyenne_finale"].mean() else "Classe B"

#Meilleur Etudient
best_A = classeA.loc[classeA["Moyenne_finale"].idxmax(), ["nom","Moyenne_finale"]]
best_B = classeB.loc[classeB["Moyenne_finale"].idxmax(), ["nom","Moyenne_finale"]]

#Moyenne par sexe
moyenne_sexe_A = classeA.groupby("sexe")["Moyenne_finale"].mean()
moyenne_sexe_B = classeB.groupby("sexe")["Moyenne_finale"].mean()

# Affichage des Résultatls
print("Classe meilleure:", classe_better)
print("\nMeilleur étudiant Classe A:", best_A.to_dict())
print("Meilleur étudiant Classe B:", best_B.to_dict())
print("\nMoyenne par sexe Classe A:\n", moyenne_sexe_A.to_dict())
print("Moyenne par sexe Classe B:\n", moyenne_sexe_B.to_dict())

import matplotlib.pyplot as plt 

# Histogramme : la distribution des moyennes finales des deux classes
plt.figure(figsize=(10,5)) 
plt.hist(classeA["Moyenne_finale"], bins=10, alpha=0.5, label="Classe A") 
plt.hist(classeB["Moyenne_finale"], bins=10, alpha=0.5, label="Classe B") 
plt.title("Distribution des Moyennes Finales") 
plt.xlabel("Moyenne finale") 
plt.ylabel("Nombre d'étudiants") 
plt.legend() 
plt.savefig("figures/fig1.png")
plt.show()


# Nuage de points : la relation entre la somme des notes des DS et la note du projet pour chaque classe
plt.figure(figsize=(8,5)) 
plt.scatter(classeA["DS1"] + classeA["DS2"] + classeA["DS3"], classeA["Projet"], label="Classe A", color='blue') 
plt.scatter(classeB["DS1"] + classeB["DS2"] + classeB["DS3"], classeB["Projet"], label="Classe B", color='orange') 
plt.title("Projet vs Somme des DS") 
plt.xlabel("Somme des DS") 
plt.ylabel("Projet") 
plt.legend() 
plt.savefig("figures/fig2.png")
plt.show()


# Ligne : la moyenne finale de chaque étudiant dans les deux classes
plt.figure(figsize=(10,5)) 
classeA_sorted = classeA.sort_values("Moyenne_finale") 
classeB_sorted = classeB.sort_values("Moyenne_finale") 
plt.plot(classeA_sorted["nom"], classeA_sorted["Moyenne_finale"], marker='o', label='Classe A') 
plt.plot(classeB_sorted["nom"], classeB_sorted["Moyenne_finale"], marker='o', label='Classe B') 
plt.xticks(rotation=90) 
plt.title("Moyenne finale par étudiant") 
plt.xlabel("Nom de l'étudiant") 
plt.ylabel("Moyenne finale") 
plt.legend() 
plt.savefig("figures/fig3.png")
plt.show()