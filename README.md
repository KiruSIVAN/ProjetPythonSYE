# ProjetPythonSYE

## Parallélisation Maximale Automatique

Développer une libraire en Python pour automatiser la parallélisation maximale de systèmes de tâches. L’utilisateur doit pouvoir spécifier des tâches quelconques, interagissant
à travers un ensemble arbitraire de variables, et pouvoir :
1. obtenir le système de tâches de parallélisme maximal réunissant les tâches en entrée,
2. exécuter le système de tâches de façon séquentielle, tout en respectant les contraintes de précédence,
3. exécuter le système de tâches en parallèle, tout en respectant les contraintes de précédence.


### Importation des packages

**Grazphviz :** créer des graphes et de les répresenter sous formes de diagrammes
> import digraph : créer des graphes orientés

**Rich :** pour une meilleure présentation des résultats de la console
> import rprint : afficher du texte dans la console

> import time : pour manipuler le temps
> import random : pour générer des valeurs aléatoires
