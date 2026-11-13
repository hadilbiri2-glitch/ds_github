taches = []
prochain_id = 1


def afficher_menu():
    print("\n========== GESTION DES TACHES ==========")
    print("1. Ajouter une tache")
    print("2. Afficher toutes les taches")
    print("3. Rechercher une tache")
    print("4. Modifier une tache")
    print("0. Quitter")
    print("========================================")


def saisir_texte(message):
    while True:
        valeur = input(message).strip()
        if valeur:
            return valeur
        print("Erreur : cette information ne peut pas etre vide.")


def ajouter_tache():
    global prochain_id

    print("\n--- Ajouter une tache ---")
    titre = saisir_texte("Titre : ")
    description = input("Description (facultative) : ").strip()

    tache = {
        "id": prochain_id,
        "titre": titre,
        "description": description,
        "terminee": False
    }

    taches.append(tache)
    prochain_id += 1
    print("La tache a ete ajoutee avec succes.")


def afficher_taches():
    print("\n--- Liste des taches ---")

    if not taches:
        print("Aucune tache pour le moment.")
        return

    for tache in taches:
        statut = "Terminee" if tache["terminee"] else "En cours"
        print("----------------------------------------")
        print("ID :", tache["id"])
        print("Titre :", tache["titre"])
        print("Description :", tache["description"] or "Aucune")
        print("Statut :", statut)
    print("----------------------------------------")


def rechercher_tache():
    print("\n--- Rechercher une tache ---")

    if not taches:
        print("La liste des taches est vide.")
        return

    mot_cle = saisir_texte("Saisir le titre ou un mot-cle : ").lower()
    resultats = []

    for tache in taches:
        if mot_cle in tache["titre"].lower():
            resultats.append(tache)

    if not resultats:
        print("Aucune tache correspondante.")
    else:
        print("Resultat(s) de la recherche :")
        for tache in resultats:
            statut = "Terminee" if tache["terminee"] else "En cours"
            print(f"ID : {tache['id']} | Titre : {tache['titre']} | Statut : {statut}")


def trouver_tache_par_id(identifiant):
    for tache in taches:
        if tache["id"] == identifiant:
            return tache
    return None


def modifier_tache():
    print("\n--- Modifier une tache ---")

    if not taches:
        print("Aucune tache a modifier.")
        return

    afficher_taches()

    try:
        identifiant = int(input("Saisir l'ID de la tache a modifier : "))
    except ValueError:
        print("Erreur : l'ID doit etre un nombre entier.")
        return

    tache = trouver_tache_par_id(identifiant)

    if tache is None:
        print("Erreur : aucune tache ne possede cet ID.")
        return

    print("Laisser le champ vide pour conserver l'ancienne valeur.")
    nouveau_titre = input(f"Nouveau titre [{tache['titre']}] : ").strip()
    nouvelle_description = input(
        f"Nouvelle description [{tache['description']}] : "
    ).strip()

    if nouveau_titre:
        tache["titre"] = nouveau_titre
    if nouvelle_description:
        tache["description"] = nouvelle_description

    print("La tache a ete modifiee avec succes.")


def main():
    while True:
        afficher_menu()

        try:
            choix = int(input("Votre choix : "))
        except ValueError:
            print("Erreur : veuillez saisir un nombre parmi les choix du menu.")
            continue

        if choix == 1:
            ajouter_tache()
        elif choix == 2:
            afficher_taches()
        elif choix == 3:
            rechercher_tache()
        elif choix == 4:
            modifier_tache()
        elif choix == 0:
            print("Merci d'avoir utilise l'application. Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir une option du menu.")

main()
#test terminer