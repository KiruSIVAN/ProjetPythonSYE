# ProjetPythonSYE

## Parallélisation Maximale Automatique

Développer une libraire en Python pour automatiser la parallélisation maximale de systèmes de tâches. L’utilisateur doit pouvoir spécifier des tâches quelconques, interagissant à travers un ensemble arbitraire de variables, et pouvoir :
1. obtenir le système de tâches de parallélisme maximal réunissant les tâches en entrée,
2. exécuter le système de tâches de façon séquentielle, tout en respectant les contraintes de précédence,
3. exécuter le système de tâches en parallèle, tout en respectant les contraintes de précédence.

## Fichier maxpar.py :

### Importation des packages

**Grazphviz :** créer des graphes et de les répresenter sous formes de diagrammes
> import digraph : créer des graphes orientés

**Rich :** pour une meilleure présentation des résultats de la console
> import rprint : afficher du texte dans la console

> import time : pour manipuler le temps
> import random : pour générer des valeurs aléatoires


### L'ensemble des classes
**- Task :** la classe Task représente une tâche, possèdant  une méthode spéciale __init__ qui est appelée lors de la création d'une instance.
>"name" : le nom de la tâche, unique dans un système de tâche donné;
>"reads" : le domaine de lecture de la tâche;
>"writes" : le domaine d’écriture de la tâche;
>"run" : la fonction qui déterminera le comportement de la tâche;

**- TaskSystem :** la classe TaskSystem représente la classe principale de ce module. Elle est responsable de la gestion d'un système de tâches qui contient plusieurs tâches et leurs dépendances.

#### Validation des entrées

**Vérification 1 :** Lors de la création d'un objet TaskSystem, on vérifie si les noms des tâches sont uniques.
>On crée une liste de noms des tâches : "task_names", puis on compare la longueur de la liste set(task_names),qui contient que des éléments uniques avec la liste d'origine.
**Vérification 2 :** Lors de la création d'un objet TaskSystem, on vérifie s'il y a des tâches inconnues dans les dépendances.
>On parcourt toutes les listes de dépendances du dictionnaire, puis on parcourt chaque dépendance dans la liste de dépendances et on vérifie si les noms de tâches référencées se trouvent dans la liste des noms de tâches.

#### Les méthodes

**— getDependencies(nomTache) :** pour un nom de tâche donné, renvoie la liste desnoms des tâches qui doivent s’exécuter avant la tâche nomTache selon le système de parallélisme maximale.

**— runSeq() :** exécute les tâches du système de façon séquentielle en respectant l’ordre imposé par la relation de précédence.

**— run() :** exécute les tâches du système en parallélisant celles qui peuvent être parallélisées selon la spécification du parallélisme maximale.
> On commence par créer un ensemble des tâches à exécuter et un ensemble vide pour stocker des tâches déjà complétées. On utilise la boucle while pour exécuter les tâches jusqu'à ce qu'il n'y ait plus à exécuter. Pour chaque tâche, on récupère ses dépendances. Si toutes les dépendances ont été exécutées, on éxecute la tâche et on l'ajoute à la liste des tâches complétées. sinon, on éxecute les dépendances, puis on exécute les tâches. On les ajoute à la liste des tâches complétées.

**— draw(Filename) :** trace le graphe des tâches à l'aide de Graphviz. Elle parcourt la liste des tâches et ajoute chaque tâche en tant que nœud au graphe. Elle parcourt ensuite le dictionnaire des dépendances et ajoute une arête entre chaque tâche et sa dépendance.

**— parCost(numTests) :** compare le temps d'exécution du système de tâches en séquentiel et en parallèle. On mesure le temps d'exécution en séquentiel en exécutant la méthode runSeq et en enregistrant le temps de début et de fin de chaque exécution dans une liste. On calcule ensuite la moyenne du temps d'exécution en séquentiel. On mesure ensuite le temps d'exécution en parallèle en exécutant la méthode run et en enregistrant le temps de début et de fin de chaque exécution dans une liste. Elle calcule ensuite la moyenne du temps d'exécution en parallèle. Enfin, elle affiche la moyenne des deux temps d'exécution.

**— detTestRnd(numTests) :** génère des valeurs aléatoires pour les variables et exécute le système de tâches. On vérifie ensuite les résultats pour chaque variable et si les valeurs sont différentes pour la même variable, alors le système n'est pas déterministe. Sinon, le système est déterministe.

## Fichier test_maxpar.py :
Le fichier permet de réaliser une parallélisation automatique. Il permet d'effectuer des tâches séquentielles et parallèles ainsi que de créer un graphe, effectuer un test de déterminisme et calculer le coût du parallélisme.

# Construction du système de tâches
s1 = TaskSystem([t1, t2, t3, t4, t5, t6, tSomme], {"T1": [], "T2": ["T1"], "T3" : ["T2"], "T4" : [], "T5" : ["T4"],"T6" : [ "T4"], "somme": [ "T5", "T6" ]})

![Le graphe orienté obtenu de s1 à l'aide du GraphViz ](https://raw.githubusercontent.com/KiruSIVAN/ProjetPythonSYE/main/maxpar.png)

s1 est un système de tâches qui prend deux paramètres. En premier argument, l'ensemble des tâches. Le dictionnaire de précédence passé en deuxième argument au constructeur précise que la tâche dont le nom est "T2" doit s’exécuter après celle qui a le nom "T1", la tâche "T3" doit s’exécuter après celle qui a le nom "T2", la tâche "T5" doit s’exécuter après celle qui a le nom "T4", la tâche "T6" doit s’exécuter après celle qui a le nom "T4", De la même façon, la tâche dont le nom est "somme" doit s’exécuter après les tâches "T5" et "T6".

![Le digraph obtenu de s1 à l'aide du GraphViz ](https://raw.githubusercontent.com/KiruSIVAN/ProjetPythonSYE/main/digraph.png)
