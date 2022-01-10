import sys
import time
from itertools import combinations
from pprint import pprint as pp
from utils import read_and_clean_csv
from utils import write_on_csv

BUDGET = 500


def bruteforce(action_list):
    """
    Fonction qui trouve toutes les différentes combinaisons d'actions possibles.
    Calcule le coût et le bénéfice total de chaque combinaison.
    Écrit le résultat dans un fichier csv puis le retourne sous forme de liste.

    Paramètres
    ----------
    action_list (list) : Liste d'actions.

    Retour
    ------
    Retourne la liste de toutes les combinaisons d'actions possibles.
    """
    comb = []
    for i in range(0, len(action_list)+1):
        comb += list(combinations(action_list, i))
    possibilities = []
    for c in comb:
        dict_tmp = {}
        total_cost = 0
        gain = 0
        for action in action_list:
            if action not in c:
                dict_tmp[action[0]] = "NO BUY"
            else:
                dict_tmp[action[0]] = "BUY"
                total_cost += float(action[1]) / 100
                gain += float(action[3]) / 100
        dict_tmp["Investissement"] = total_cost
        dict_tmp["Gain"] = gain
        possibilities.append(dict_tmp)
    write_on_csv(possibilities, BUDGET)
    return possibilities


def best_investment(possibilities):
    """
    Fonction qui explore toutes les combinaisons d'actions possibles
    et affiche la liste des meilleures actions à acheter.

    Paramètres
    ----------
    possibilities (list) : Liste de toutes les combinaisons d'actions possibles.

    Retour
    ------
    Retoune la liste des meilleures actions à acheter, le gain et total.
    """
    best_decision = {}
    max_profit = 0
    for p in possibilities:
        if p["Investissement"] <= BUDGET and p["Gain"] > max_profit:
            max_profit = p["Gain"]
            best_decision = p
    return best_decision


if __name__ == "__main__":
    file_args = sys.argv
    if len(file_args) >= 2:
        filename = file_args[1]
    else:
        filename = "data/actions.csv"
    print("------------------------ Algorithme de force brute ------------------------")
    start = time.time()
    actions = read_and_clean_csv(filename)
    possibilities = bruteforce(actions)
    pp(best_investment(possibilities))
    print(f"Temps d’exécution de l'algorithme : {time.time() - start} secondes.")
