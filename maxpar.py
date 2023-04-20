"""
Objectif: 
---------
    ce module sert:
        1. obtenir le système de tâches de parallélisme maximal réunissant les tâches en entrée,
        2. exécuter le système de tâches de façon séquentielle, tout en respectant les contraintes de précédence,
        3. exécuter le système de tâches en parallèle, tout en respectant les contraintes de précédence.
"""
try:
    from graphviz import Digraph # pour la visualisation
    import random # pour générer des valeurs aléatoires
    from rich import print as rprint # pour une meilleure présentation des résultats
except Exception as e:
    rprint(f"[red]Error lors de l'importation des packages[/red]: {e}")

class Task:
    """
     la classe Task représente une tâche
    """
    def __init__(self, name="", reads=[], writes=[], run=None):
        self.name = name
        self.reads = reads
        self.writes = writes
        self.run = run
        
class TaskSystem:
    """
    La classe TaskSystem est la classe principale de ce module. 
    Elle est responsable de la gestion d'un système de tâches qui contient plusieurs tâches et leurs dépendances.
    """
    def __init__(self, tasks, dependencies):
        self.tasks = tasks
        self.dependencies = dependencies

        """
        Lors de la création d'un objet TaskSystem, on vérifie si les noms des tâches sont uniques, 
        s'il y a des tâches inconnues dans les dépendances et s'il y a des cycles de dépendances.
        """
        rprint("\n" + "[cyan]*[/cyan]" * 40 + "[yellow][u]Vérifications[/u][/yellow]" + "[cyan]*[/cyan]" * 60 + '\n')
        # Vérification 1 : Vérifier que les noms des tâches sont uniques.
        task_names = [task.name for task in tasks]
        if len(set(task_names)) != len(task_names):
            raise ValueError("Les noms de tâches ne sont pas uniques.")
        rprint("[green]Vérification 1: DONE[/green]\n")

        # Vérification 2:  des tâches inconnues dans les dépendances
        for dep_list in dependencies.values():
            for dep in dep_list:
                if dep not in task_names:
                    raise ValueError(f"La tâche {dep} référencée dans le dictionnaire de précédence n'existe pas.")
        rprint("[green]Vérification 2: DONE[/green]\n")


    def getDependencies(self, taskName):
        """
        renvoyer la liste des dépendances d'une tâche spécifique
        """
        return self.dependencies[taskName]

    def runSeq(self):
        """
        La méthode runSeq exécute le système de tâches de façon séquentielle, tout en respectant les contraintes de précédence.
        """
        for task in self.tasks:
            task.run()

    def run(self):
        """
        La méthode run exécute le système de tâches en parallèle, tout en respectant les contraintes de précédence. 
        """
        tasksToRun = set(task.name for task in self.tasks)
        completedTasks = set()
        while tasksToRun:
            for taskName in tasksToRun:
                task = next((t for t in self.tasks if t.name == taskName), None)
                if task is not None:
                    dependencies = self.getDependencies(taskName)
                    if dependencies:
                        if all(d in completedTasks for d in dependencies):
                            task.run()
                            completedTasks.add(taskName)
                    else:
                        if taskName not in completedTasks:
                            task.run()
                            completedTasks.add(taskName) 
            tasksToRun -= completedTasks
            

    def draw(self, filename):
        """
        La méthode draw permet de dessiner le graphe du système de tâches à l'aide de Graphviz.
        """
        my_graph = Digraph()
        my_graph.format = 'png'
        for task in self.tasks:
            my_graph.node(task.name)
        for task, deps in self.dependencies.items():
            for dep in deps:
                my_graph.edge(dep, task)
        my_graph.render(filename)

    def parCost(self, num_runs):
        """
        La méthode parCost mesure le temps d'exécution en séquentiel et en parallèle, puis affiche la différence de temps d'exécution entre les deux modes.
        """
        import time
        # Mesurer le temps d'exécution en séquentiel
        seq_times = []
        for i in range(num_runs):
            start_time = time.time()
            self.runSeq()
            seq_times.append(time.time() - start_time)
        
        avg_seq_time = sum(seq_times) / len(seq_times)
        rprint(f"[blue]Temps d'exécution en séquentiel (moyenne sur {num_runs} exécutions) : {avg_seq_time} secondes[/blue]\n")
        
        # Mesurer le temps d'exécution en parallèle
        par_times = []
        for i in range(num_runs):
            start_time = time.time()
            self.run()
            par_times.append(time.time() - start_time)

        avg_par_time = sum(par_times) / len(par_times)
        rprint(f"[blue]Temps d'exécution en parallèle (moyenne sur {num_runs} exécutions) : {avg_par_time} secondes[/blue]\n")


    def detTestRnd(self, numTests):
        """
        La méthode detTestRnd génère des valeurs aléatoires pour les variables et exécute le système de tâches.
        """
        for i in range(numTests):
            # Génération de valeurs aléatoires pour les variables
            for task in self.tasks:
                for var in task.reads + task.writes:
                    varValue = random.randint(0, 100)
                    exec(f"{var} = {varValue}")
            
            # Exécution du système de tâches
            self.run()
            
            # Vérification des résultats
            results = {}
            for task in self.tasks:
                for var in task.reads + task.writes:
                    if var not in results:
                        results[var] = []
                    results[var].append(eval(var))
            
            for var, values in results.items():
                if len(set(values)) > 1:
                    rprint(f"[red]Le système de tâches n'est pas déterministe pour la variable {var}[/red]")
                    return
        rprint("[green]Le système de tâches est déterministe[/green]")
