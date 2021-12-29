import csv
from itertools import combinations
from pprint import pprint as pp

BUDGET = 500


def read_csv(file, delimiter=","):
    """
    Méthode qui permet de lire un fichier csv et de retourner
    les données récupérées.

    Paramètres
    ----------
    file : Chemin du fichier à lire

    Retour
    ------
    Retourne une liste d'actions avec leurs noms, leurs coûts
    et leurs bénéfices.
    """
    with open(file, newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        actions = []
        for row in reader:
            actions.append(row)
        return actions


def write_on_csv(data):
    """
    Méthode qui permet d'écrire des données dans un fichier csv.

    Paramètres
    ----------
    data : Données à écrire dans le fichier csv
    """
    with open('csv/bruteforce.csv', 'w', newline='', encoding='UTF8') as f:
        csv.excel.delimiter = ','
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for decision in data:
            if decision["price"] <= BUDGET:
                writer.writerow(decision)


def bruteforce(action_list):
    """
    Méthode qui essaie toutes les différentes combinaisons d'actions possibles.
    Calcule le coût et le bénéfice total de chaque combinaison.
    Écris le résultat dans un fichier csv puis le retourne.

    Paramètres
    ----------
    action_list : Liste d'actions

    Retour
    ------
    Retourne la liste de toutes les combinaisons possibles.
    """
    comb = []
    for i in range(0, len(action_list)+1):
        comb += list(combinations(action_list, i))
    possibilities = []  # List of dictionaries
    for c in comb:
        dict_tmp = {}
        price = 0
        gain = 0
        for action in action_list:
            if action not in c:
                dict_tmp[action["name"]] = "NO BUY"
            else:
                dict_tmp[action["name"]] = "BUY"
                price += float(action["price"])
                gain += float(action["price"]) * float(action["profit"]) / 100
        dict_tmp["price"] = price
        dict_tmp["gain"] = gain
        possibilities.append(dict_tmp)
    write_on_csv(possibilities)
    return possibilities


def best_investment(possibilities):
    """
    Méthode qui explore toutes les combinaisons d'actions possibles
    et affiche la liste des meilleures actions à acheter.

    Paramètres
    ----------
    possibilities : Liste de toutes les combinaisons d'actions possibles

    """
    best_decision = {}
    max_profit = 0
    for p in possibilities:
        if p["price"] <= BUDGET and p["gain"] > max_profit:
            max_profit = p["gain"]
            best_decision = p
    pp(best_decision)


if __name__ == "__main__":
    actions = read_csv("csv/actions.csv", delimiter=";")
    possibilities = bruteforce(actions)
    best_investment(possibilities)
