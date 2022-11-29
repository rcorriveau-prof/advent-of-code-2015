def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return [ligne.strip() for ligne in puzzle_input.readlines()]


def do_solution_2() -> int:
    ls_lignes = fn_lire_data("puzzle")

    nb_nice = 0
    for ligne in ls_lignes:
        # Lettre sandwich
        lettre_sandwich = False
        for position, lettre in enumerate(ligne):
            if position == len(ligne) - 2:  # Avant-dernière position
                break
            elif lettre == ligne[position + 2]:
                lettre_sandwich = True
                break

        if not lettre_sandwich:  # Aller plus vite
            continue

        # doublon d'une paire
        paire_doublon = False
        # Bâtir la liste de paire de lettre
        ligne_par_deux = []
        for position, lettre in enumerate(ligne):
            if position == len(ligne) - 1:  # Dernière position
                break
            ligne_par_deux.append(lettre + ligne[position + 1])

        # Vérifier s'il une paire pareil, mais pas adjacente
        for position, paire in enumerate(ligne_par_deux):
            if paire in ligne_par_deux[position + 2:]:
                paire_doublon = True

        if lettre_sandwich and paire_doublon:
            nb_nice += 1

    return nb_nice


if __name__ == "__main__":
    print(do_solution_2())

    # Réponse test : 2
