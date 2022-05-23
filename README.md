# Programme permettant d'optimiser des stratégies d'investissement à l'aide d'algorithmes
## Descriptif
**AlgoInvest&Trade** est une société financière spécialisée dans l'investissement.<br> Elle cherche à optimiser ses stratégies d'investissement à l'aide d'algorithmes, afin de dégager davantage de bénéfices pour ses clients.<br>
Ma mission était de traduire leurs besoins commerciaux en solutions techniques.<br>
J'ai donc conçu deux algorithmes qui permettent de trouver la liste des actions les plus rentables que nous devrions acheter pour maximiser le profit d'un client au bout de deux ans.<br>
Pour utiliser ces algorithmes, il faut fournir un fichier CSV contenant des informations sur les actions à analyser.


## Fichiers de données à explorer
* Dossier : **"data"**
 * Fichier : **"actions.csv"** - (fichier CSV contenant 20 actions).<br>
 * Fichier : **"dataset1.csv"** - (fichier CSV contenant 1000 actions).<br>
 * Fichier : **"dataset2.csv"** - (ichier CSV contenant 1000 actions).<br>

## Algorithme de force brute (bruteforce.py)
Le premier fichier **bruteforce.py** contient l'algorithme de force brute.<br>

Cet algorithme va lire un fichier CSV contenant des informations sur les actions.<br> Il va trouver toutes les combinaisons d’actions possibles en tenant compte de nos contraintes puis les explorer pour afficher la combinaison d'actions représentant le meilleur investissement.<br>
L'algorithme de force brute générera un fichier **bruteforce.csv** dans lequel seront stockées toutes les combinaisons possibles.<br>
Puisque toutes les combinaisons sont testées, cet algorithme trouve la solution optimale.<br>
Mais ce n'est pas le plus optimisé car il a besoin de beaucoup de temps pour les mégadonnées.<br>
Son temps d’exécution est raisonnable uniquement pour une petite quantité de données.


## Algorithme glouton et dynamique (optimized.py)
Le deuxième fichier **optimized.py** contient les deux algorithmes optimisés.<br>

Le premier est un algorithme de type "glouton".<br>
Il est plus simple à mettre en place et son temps d'exécution est plus rapide, mais sa solution est moins optimale en terme de rentabilité.

Le deuxième est un algorithme de type "dynamique".<br>
Il est plus complexe car il utilise la programmation dynamique.<br> Cet algorithme crée une matrice. Dans cette matrice, nous stockons des solutions optimales et pour obtenir la prochaine, nous devons utiliser la solution optimale précédente.<br>

## Prérequis
* Python 3.9 ( lien de téléchargement: <https://www.python.org/downloads>)

## Installation du programme

Après avoir téléchargé le dossier **Create_Algorithms_To_Optimize_Investment_Strategies-master.zip** depuis ce lien [GitHub](https://github.com/SelHel/Create_Algorithms_To_Optimize_Investment_Strategies.git).  
Extraire les fichiers dans un dossier de votre choix.  
Ensuite, en utilisant le terminal sous Mac/Linux ou l'invite de commandes sous Windows :

* Placez vous dans le dossier courant.
* Créez un environnement virtuel :

```
python -m venv <your-virtual-env-name>
```
* Activez votre environnement virtuel sous Windows :

```
<your-virtual-env-name>\Scripts\activate.bat
```
* Activez votre environnement virtuel sous Mac/Linux :

```
source <your-virtual-env-name>/bin/activate
```
## Exécution du programme
Pour exécuter l'application utilisez le terminal sous Mac/Linux ou l'invite de commandes sous Windows puis dans le dossier courant lancez le script suivant :

* Pour l'algorithme de force brute


```
python bruteforce.py <chemin du fichier à explorer "exemple: data/actions.csv">
(si non renseigné, par défaut data/actions.csv)

```

* Pour les algorithmes optimisés


```
python optimized.py <chemin du fichier à explorer "exemple: data/dataset2.csv">
(si non renseigné, par défaut data/actions.csv)

```
Les résultats s'afficheront dans le terminal avec les informations suivantes :

* Le nom de l'algorithme
* La liste des meilleures actions à acheter
* Le gain total
* L'investissement total
* Le temps d'exécution de l'algorithme

## Auteur
**Selim Helaoui**
