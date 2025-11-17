# Objectif
# Utiliser des données de type 3 (opendata)
# Manipuler un fichier CSV
# Utiliser les boucles et agorithmie


# On utilise le fichier disponible sur
# https://www.data.gouv.fr/datasets/effectifs-deleves-par-niveau-et-nombre-de-classes-par-ecole-date-dobservation-au-debut-du-mois-doctobre-chaque-annee/



# Ouverture du fichier
file = open("fr-en-ecoles-effectifs-nb_classes.csv")
lines = file.readlines()
file.close()


# 1/ Compter le nombre de lignes

nb_lignes = 0
for line in lines[1:]:
    nb_lignes += 1
print("Le nombre de lignes de data du fichier est : ",nb_lignes)


# 2/ Compter le nombre moyen d'élève par classe (au global)
moy_cp = 0
moy_ce1 = 0
moy_ce2 = 0
moy_cm1 = 0
moy_cm2 = 0
nb_lignes = 0
for line in lines[1:]:
    data = line.strip().split(";")
    try:
        nb_cp = int(data[22])
        nb_ce2 = int(data[24])
        nb_ce1 = int(data[23])
        nb_cm1 = int(data[25])
        nb_cm2 = int(data[26])
    except Exception as e:
        print("Erreur sur ligne ",nb_lignes,e)
        continue
    moy_cp +=  nb_cp
    moy_ce1 += nb_ce1
    moy_ce2 += nb_ce2
    moy_cm1 += nb_cm1
    moy_cm2 += nb_cm2
    nb_lignes += 1
moy_cp /= nb_lignes
moy_ce1 /= nb_lignes
moy_ce2 /= nb_lignes
moy_cm1 /= nb_lignes
moy_cm2 /= nb_lignes

print("Nombre moyen d'élèves en CP :",moy_cp)
print("Nombre moyen d'élèves en CE1 :",moy_ce1)
print("Nombre moyen d'élèves en CE2 :",moy_ce2)
print("Nombre moyen d'élèves en CM1 :",moy_cm1)
print("Nombre moyen d'élèves en CM2 :",moy_cm2)



# 2/ Compter le nombre moyen d'élève par classe et par année
niveaux = ['cp','ce1','ce2','cm1','cm2']
annee_min = 2013
annee_max = 2022
moy = {}
nb_lignes = {annee:0 for annee in range(annee_min,annee_max+1)}

# Initialisation
for niveau in niveaux:
    moy[niveau] = {}
    for annee in range(annee_min,annee_max+1):
        moy[niveau][annee] = 0

# Parcours du fichier
for line in lines[1:]:
    data = line.strip().split(";")
    try:
        annee = int(data[0])
        if annee < annee_min or annee > annee_max:
            continue
        nb_cp = int(data[22])
        nb_ce1 = int(data[23])
        nb_ce2 = int(data[24])
        nb_cm1 = int(data[25])
        nb_cm2 = int(data[26])
    except Exception as e:
        print("Erreur sur ligne ",nb_lignes,e)
        continue
    moy['cp'][annee] += nb_cp
    moy['ce1'][annee] += nb_ce1
    moy['ce2'][annee] += nb_ce2
    moy['cm1'][annee] += nb_cm1
    moy['cm2'][annee] += nb_cm2
    nb_lignes[annee] += 1

for annee in range(annee_min,annee_max+1):
    for niveau in niveaux:
        moy[niveau][annee] /= nb_lignes[annee]

for niveau in niveaux:
    for annee in range(annee_min,annee_max+1):
        print(f"{annee} Nombre moyen d'élèves en {niveau} : {moy[niveau][annee]}")


# Affichage avec matplotlib

# Pour trier les années, il faut reconstruire les tableaux de valeurs
niveau = 'cp'
tab_annees = sorted(moy[niveau].keys())
tab_valeurs = [moy[niveau][annee] for annee in tab_annees]

# Tracé
import matplotlib.pyplot as plt
plt.plot(tab_annees, tab_valeurs, marker='o')
plt.xlabel("Année")
plt.ylabel("Valeur")
plt.title("Valeurs par année")
plt.grid(True)
plt.show()

