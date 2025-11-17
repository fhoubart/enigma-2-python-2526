# On utilise le fichier disponible sur
# https://www.data.gouv.fr/datasets/effectifs-deleves-par-niveau-et-nombre-de-classes-par-ecole-date-dobservation-au-debut-du-mois-doctobre-chaque-annee/



# Ouverture du fichier
file = open("fr-en-ecoles-effectifs-nb_classes.csv")
lines = file.readlines()
file.close()


# 2/ Compter le nombre moyen d'élève par classe et par année
niveaux = ['cp','ce1','ce2','cm1','cm2']
annees = []
regions = []
moy = {niveau:{} for niveau in niveaux}
nb_lignes = {}

# Numéro de la ligne pour affichage d'erreur
index_ligne = 0

# Parcours du fichier
for line in lines[1:]:
    index_ligne += 1
    data = line.strip().split(";")
    try:
        annee = int(data[0])
        region = data[7]

        # Si region inconnue, ajout dans les différents dictionnaires
        if not region in regions:
            regions.append(region)
            for niveau in niveaux:
                for annee in annees:
                    moy[niveau][annee][region] = 0
            for annee in annees:
                nb_lignes[annee][region] = 0

        # Si annee inconnue, ajout de l'année dans les différents dictionnaires
        if not annee in annees:
            annees.append(annee)
            annees = sorted(annees)
            for niveau in niveaux:
                moy[niveau][annee] = {region:0 for region in regions}
            nb_lignes[annee] = {region:0 for region in regions}

        # Calcul des différents nombre d'élèves par niveau
        nb = {
            'cp': int(data[22]),
            'ce1': int(data[23]),
            'ce2': int(data[24]),
            'cm1': int(data[25]),
            'cm2': int(data[26])
        }

    except Exception as e:
        # Cas ou la ligne pose un problème de format, on l'ignore
        print("Erreur sur ligne ",index_ligne,e)
        continue

    # Ici, les différents nombre d'élèves par niveau ont été bien calculés sans erreurs
    for niveau in niveaux:
        moy[niveau][annee][region] += nb[niveau]
    nb_lignes[annee][region] += 1


# Division par le nombre de lignes pour calculer les moyennes
for annee in annees:
    for niveau in niveaux:
        for region in regions:
            if nb_lignes[annee][region] > 0:
                moy[niveau][annee][region] /= nb_lignes[annee][region]

# Affichage des resultats
for niveau in niveaux:
    for annee in annees:
        for region in ['AIN','AINES']:
            print(f"{annee} Nombre moyen d'élèves en {niveau} dans f{region}: {moy[niveau][annee]}")


# Recherche pour chaque année de la région avec la plus grande moyenne d'élève par classe de CP
niveau = 'cp'
# Pour chaque année, on mémorise le nom de la région et le nombre moyen d'élève le plus grand, qui sera
# testé successivement sur toutes les données pour ne conserver que la plus grande
plus_grande_region = {
    annee:{
        'region':"",
        'nb_eleves':0}
    for annee in annees}

for annee in annees:
    for region in regions:
        if moy[niveau][annee][region] > plus_grande_region[annee]['nb_eleves']:
            plus_grande_region[annee]['region'] = region
            plus_grande_region[annee]['nb_eleves'] = moy[niveau][annee][region]

# Affichage des résultats
for annee in annees:
    print(f"La région avec le plus grand nombre moyen d'élève par classe de CP en {annee} est le/la {plus_grande_region[annee]['region']} avec {plus_grande_region[annee]['nb_eleves']}")

