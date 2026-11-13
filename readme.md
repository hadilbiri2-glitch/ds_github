# Gestionnaire de tâches - Partie 1

Ce projet est une application console simple développée en Python permettant de gérer des tâches directement en mémoire vive[cite: 1].

## Fonctionnalités

Le programme propose un menu interactif comportant les options suivantes[cite: 1] :
* **1. Ajouter une tâche** : Permet de créer une nouvelle tâche en renseignant un titre, une description facultative, une échéance et une priorité[cite: 1].
* **2. Afficher les tâches** : Permet de lister l'ensemble des tâches enregistrées avec leur identifiant, titre, description, échéance, priorité et état ("à faire" ou "terminée")[cite: 1].
* **3. Rechercher une tâche** : Permet de filtrer et trouver des tâches à l'aide d'un mot-clé présent dans le titre ou la description[cite: 1].
* **4. Modifier une tâche** : Permet de mettre à jour les informations d'une tâche existante à partir de son identifiant[cite: 1].
* **0. Quitter** : Permet de fermer l'application[cite: 1].

## Caractéristiques techniques

* **Données en mémoire** : Les données sont stockées dans une liste dynamique (les tâches sont réinitialisées à la fermeture du programme)[cite: 1].
* **Niveaux de priorité** : Le système gère trois niveaux de priorité : `basse`, `moyenne` et `haute`[cite: 1].
* **Saisies sécurisées et contrôlées** : Le script intègre des fonctions de validation robustes pour les textes, les nombres entiers, les dates au format `JJ/MM/AAAA` et les priorités[cite: 1].

## Prérequis

* Python 3.x installé sur votre machine[cite: 1].

## Utilisation

Pour lancer le gestionnaire de tâches, exécutez la commande suivante dans votre terminal :

```bash
python gestionnaire_taches.py