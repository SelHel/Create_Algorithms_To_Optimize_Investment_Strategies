from pprint import pprint as pp
from bruteforce import read_csv

BUDGET = 500


def optimized(file, delimiter=","):
    action_list = read_csv(file, delimiter=delimiter)
    action_list.sort(key=lambda x: float(x["profit"]), reverse=True)
    best_decision = {"actions": []}
    price = 0
    gain = 0
    for action in action_list:
        if price + float(action["price"]) <= BUDGET:
            price += float(action["price"])
            gain += float(action["price"]) * float(action["profit"]) / 100
            best_decision["actions"].append(action["name"])
    best_decision["price"] = price
    best_decision["gain"] = gain
    pp(best_decision)


if __name__ == "__main__":
    optimized("csv/actions.csv", delimiter=";")
