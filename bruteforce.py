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
        price = 0
        gain = 0
        for action in action_list:
            if action not in c:
                dict_tmp[action[0]] = "NO BUY"
            else:
                dict_tmp[action[0]] = "BUY"
                price += float(action[1]) / 100
                gain += float(action[2]) / 100
        dict_tmp["price"] = price
        dict_tmp["gain"] = gain
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
    """
    best_decision = {}
    max_profit = 0
    for p in possibilities:
        if p["price"] <= BUDGET and p["gain"] > max_profit:
            max_profit = p["gain"]
            best_decision = p
    pp(best_decision)


if __name__ == "__main__":
    start = time.time()
    actions = read_and_clean_csv("csv/actions.csv")
    possibilities = bruteforce(actions)
    best_investment(possibilities)
    print(f"Temps d’exécution de la fonction : {time.time() - start} secondes.")
