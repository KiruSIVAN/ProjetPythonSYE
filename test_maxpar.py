"""
Objectif: 
---------
    ce script sert à tester "maxpar.py"
"""
try:
    from maxpar import Task, TaskSystem
    from rich import print as rprint
except Exception as e:
    print(f"Error lors de l'importation des packages: {e}")

rprint ("==================================================================================================================")
rprint ("=                                            [green][u]Libraire en Python[/u][/green]                                                  =")
rprint ("=                                    [yellow][u]Parallélisation maximale automatique[/u][/yellow]                                        =")
rprint ("=                                 [red][u]Projet pratique en Systèmes d'exploitation[/u][/red]                                     =")
rprint ("==================================================================================================================\n")

# Initialisation de variables 
A = None
B = None
C = None
D = None
E = None
F = None
G = None

# Les fonctions
def runT1():
    global A
    A = 1

def runT2():
    global B
    B = 5

def runT3():
    global C, A, B
    C = A + B

def runT4():
    global D
    D = 2

def runT5():
    global E
    E = 5

def runT6():
    global F, D
    F = D + D

def runTsomme():
    global G, E, F
    G = E + F

# Construction deS tâches
t1 = Task(name="T1", writes=["A"], run=runT1)
t2 = Task(name="T2", writes=["B"], run=runT2)
t3 = Task(name="T3", reads=["A", "B"], writes=["C"], run=runT3)
t4 = Task(name="T4", writes=["D"], run=runT4)
t5 = Task(name="T5", writes=["E"], run=runT5)
t6 = Task(name="T6", reads=["D"], writes=["F"], run=runT6)
tSomme = Task(name="somme", reads=["E", "F"], writes=["G"], run=runTsomme)

# Construction du système de tâches
s1 = TaskSystem([t1, t2, t3, t4, t5, t6, tSomme], {"T1": [], "T2": ["T1"], "T3" : ["T2"], "T4" : [], "T5" : ["T4"],"T6" : [ "T4"], "somme": [ "T5", "T6" ]})

# Exécution séquentielle
rprint("\n" + "[cyan]*[/cyan]" * 40 + "[yellow][u]Exécution séquentielle[/u][/yellow]" + "[cyan]*[/cyan]" * 51 + '\n')
s1.runSeq()
rprint(f"[blue]Les nouvelles valeurs sont: A = {A}, B = {B}, C = {C}, D = {D}, E = {E}, F = {F}, G = {G} [/blue]")

# Réinitialisation des variables X, Y, Z
A = None
B = None
C = None
D = None
E = None
F = None
G = None

# Exécution parallèle
rprint("\n" + "[cyan]*[/cyan]" * 40 + "[yellow][u]Exécution parallèle[/u][/yellow]" + "[cyan]*[/cyan]" * 54 + '\n')
s1.run()
rprint(f"[blue]Les nouvelles valeurs sont: A = {A}, B = {B}, C = {C}, D = {D}, E = {E}, F = {F}, G = {G} [/blue]")

# Affichage du Graphe
rprint("\n" + "[cyan]*[/cyan]" * 40 + "[yellow][u]Affichage du graphe[/u][/yellow]" + "[cyan]*[/cyan]" * 54 + '\n')
s1.draw('maxpar')
rprint(f"[blue]maxpar.png[/blue] est disponible ")

# Coût du parallélisme
rprint("\n" + "[cyan]*[/cyan]" * 40 + "[yellow][u]Coût du parallélisme[/u][/yellow]" + "[cyan]*[/cyan]" * 53 + '\n')
s1.parCost(9999)
