import csv
from itertools import combinations

BUDGET = 500


def get_data_from_csv(file):
    """
    Méthode qui permet de lire un fichier csv et de retourner les données récupérées.

    Paramètres
    ----------
    file : Chemin du fichier à lire

    Retour
    ------
    Retourne une liste d'actions avec leurs noms, leurs coûts et leurs bénéfices.
    """
    with open(file, newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        actions = []
        for row in reader:
            actions.append(row)
        return actions


def create_list_all_cases(actions):
    """
    Méthode qui essaie toutes les différentes combinaisons d'actions possibles.

    Paramètres
    ----------
    actions : Liste des actions

    Retour
    ------
    Retourne une liste de toutes les combinaisons possibles.
    """
    if len(actions) == 1:
        return [
            {
                actions["name"]: "Buy"
            },
            {
                actions["name"]: "No Buy"
            },
        ]