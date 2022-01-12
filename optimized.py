import time
import sys
from pprint import pprint as pp
from utils import read_and_clean_csv

BUDGET = 50000


def greedy(file):
    """
    Fonction qui permet de lire un fichier csv puis de trier une liste d'actions
    pour sélectionner et afficher la meilleure solution d'investissement.

    Paramètres
    ----------
    file (str) : Chemin du fichier à lire

    Retour
    ------
    Retourne la liste des meilleures actions à acheter, le gain et l'investissement total.
    """
    action_list = read_and_clean_csv(file)
    action_list.sort(key=lambda x: float(x[1]), reverse=True)
    action_list.sort(key=lambda x: float(x[2]), reverse=True)
    best_decision = {"Actions": []}
    total_cost = 0
    gain = 0
    for action in action_list:
        if total_cost + float(action[1]) <= BUDGET:
            total_cost += float(action[1])
            gain += float(action[3])
            best_decision["Actions"].append(action[0])
    best_decision["Investissement"] = total_cost / 100
    best_decision["Gain"] = gain / 100
    return best_decision


def knapsack(budget, action_list):
    """
    Fonction qui à partir d'une matrice, va déterminer la meilleure solution d'investissement.

    Paramètres
    ----------
    budget (int) : Budget client en centimes pour éviter les virgules.
    action_list (list) : Liste des actions avec nom, prix et profit en centimes pour éviter les virgules.

    Retour
    ------
    Retourne le bénéfice total et la liste des meilleures actions à acheter.
    """
    matrix = [[0 for x in range(budget + 1)] for x in range(len(action_list) + 1)]
    for action in range(1, len(action_list) + 1):
        for invest in range(1, budget + 1):
            if action_list[action - 1][1] <= invest:
                matrix[action][invest] = max(action_list[action - 1][3] + matrix[action - 1]
                                             [invest-action_list[action - 1][1]],
                                             matrix[action - 1][invest])
            else:
                matrix[action][invest] = matrix[action - 1][invest]

    investment = budget
    n = len(action_list)
    best_decision = []
    while investment >= 0 and n >= 0:
        a = action_list[n - 1]
        if matrix[n][investment] == matrix[n - 1][investment - a[1]] + a[3]:
            best_decision.append((a[0], a[1] / 100, round((a[3] / 100), 2)))
            investment -= a[1]
        n -= 1

    total_cost = sum([item[1] for item in best_decision])

    return {
        "Actions": [item[0] for item in best_decision],
        "Gain": round((matrix[-1][-1] / 100), 2),
        "Investissement": total_cost
    }


if __name__ == "__main__":
    file_args = sys.argv
    if len(file_args) >= 2:
        filename = file_args[1]
    else:
        filename = "data/actions.csv"

    print("------------------------ Algorithme glouton ------------------------")
    start = time.time()
    pp(greedy(filename))
    print(f"Temps d’exécution de l'algorithme : {time.time() - start} secondes.")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")

    print("------------------------ Algorithme sac à dos ------------------------")
    start = time.time()
    action_list = read_and_clean_csv(filename)
    pp(knapsack(BUDGET, action_list))
    print(f"Temps d’exécution de l'algorithme : {time.time() - start} secondes.")
