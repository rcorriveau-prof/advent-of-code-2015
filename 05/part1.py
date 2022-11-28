def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return [ligne.strip() for ligne in puzzle_input.readlines()]


def do_solution_1() -> int:
    ls_lignes = fn_lire_data("puzzle")

    nb_nice = 0
    for ligne in ls_lignes:
        # Vérifier chaines interdites
        chaine_interdite = False
        for position, lettre in enumerate(ligne):
            if position == len(ligne) - 1:
                break
            elif lettre + ligne[position + 1] in ("ab", "cd", "pq", "xy"):
                chaine_interdite = True
                break
        if chaine_interdite:
            continue

        # Compter voyelles
        voyelles = len([lettre for lettre in ligne if lettre in "aeiou"]) >= 3

        # Vérifier double lettre
        doublon = False
        for position, lettre in enumerate(ligne):
            if position == len(ligne) - 1:
                break
            elif lettre == ligne[position + 1]:
                doublon = True
                break

        if voyelles and doublon:
            nb_nice += 1

    return nb_nice


if __name__ == "__main__":
    print(do_solution_1())

    # Réponse test : 2
