"""
Objectif: 
---------
    ce script sert à tester "maxpar.py"
"""
try:
    from maxpar import Task, TaskSystem
    from rich import print as rprint
    import os
except Exception as e:
    print(f"Error lors de l'importation des packages: {e}")

#Clear Screen
os.system('clear')

rprint ("==================================================================================================================")
rprint ("=                                            [green][u]Libraire en Python[/u][/green]                                                  =")
rprint ("=                                    [yellow][u]Parallélisation maximale automatique[/u][/yellow]                                        =")
rprint ("=                                 [red][u]Projet pratique en Systèmes d'exploitation[/u][/red]                                     =")
rprint ("==================================================================================================================\n")

# Initialisation de variables 
X = None
Y = None
Z = None

# Les fonctions
def runT1():
    global X
    X = 1

def runT2():
    global Y
    Y = 2

def runTsomme():
    global X, Y, Z
    Z = X + Y

# Construction deS tâches
t1 = Task(name="T1", writes=["X"], run=runT1)
t2 = Task(name="T2", writes=["Y"], run=runT2)
tSomme = Task(name="somme", reads=["X", "Y"], writes=["Z"], run=runTsomme)

# Construction du système de tâches
s1 = TaskSystem([t1, t2, tSomme], {"T1": [], "T2": ["T1"], "somme": ["T1", "T2"]})

# Exécution séquentielle
rprint("\n" + "[cyan]*[/cyan]" * 40 + "[yellow][u]Exécution séquentielle[/u][/yellow]" + "[cyan]*[/cyan]" * 51 + '\n')
s1.runSeq()
rprint(f"[blue]Les nouvelles valeurs sont: X = {X}, Y = {Y}, Z = {Z}[/blue]")

# Réinitialisation des variables X, Y, Z
X = None
Y = None
Z = None

# Exécution parallèle
rprint("\n" + "[cyan]*[/cyan]" * 40 + "[yellow][u]Exécution parallèle[/u][/yellow]" + "[cyan]*[/cyan]" * 54 + '\n')
s1.run()
rprint(f"[blue]Les nouvelles valeurs sont: X = {X}, Y = {Y}, Z = {Z}[/blue]")

# Affichage du Graphe
rprint("\n" + "[cyan]*[/cyan]" * 40 + "[yellow][u]Affichage du graphe[/u][/yellow]" + "[cyan]*[/cyan]" * 54 + '\n')
s1.draw('maxpar')
rprint(f"[blue]maxpar.png[/blue] est disponible ")

# Test randomisé de déterminisme
rprint("\n" + "[cyan]*[/cyan]" * 40 + "[yellow][u]Test randomisé de déterminisme[/u][/yellow]" + "[cyan]*[/cyan]" * 43 + '\n')
s1.detTestRnd(5)

# Coût du parallélisme
rprint("\n" + "[cyan]*[/cyan]" * 40 + "[yellow][u]Coût du parallélisme[/u][/yellow]" + "[cyan]*[/cyan]" * 53 + '\n')
s1.parCost(3)