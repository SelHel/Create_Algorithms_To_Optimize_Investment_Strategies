import csv


def read_and_clean_csv(file, delimiter=","):
    """
    Fonction qui permet de lire un fichier csv, de nettoyer
    les données puis de les retourner sous forme de liste.

    Paramètres
    ----------
    file (str) : Chemin du fichier à lire.

    Retour
    ------
    Retourne une liste de tuple d'actions avec leurs noms, leurs profit, leurs coûts
    et leurs bénéfices en centimes.
    """
    with open(file, newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
        action_list = []
        for row in reader:
            if float(row["price"]) > 0 and float(row["profit"]) > 0:
                price = float(row['price']) * 100
                profit = float(row['profit'])
                profit_in_cents = (profit * price) / 100
                action_list.append((row['name'], int(price), profit, profit_in_cents))
        return action_list


def write_on_csv(data, budget):
    """
    Fonction qui permet d'écrire des données dans un fichier csv.

    Paramètres
    ----------
    data (list): Données à écrire dans le fichier csv.
    """
    with open('output_csv/bruteforce.csv', 'w', newline='', encoding='UTF8') as f:
        csv.excel.delimiter = ','
        fieldnames = data[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for decision in data:
            if decision["Investissement"] <= budget:
                writer.writerow(decision)
