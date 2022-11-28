def fn_lire_data(nom_data: str) -> str:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read()


def do_solution_1() -> int:
    str_directions = fn_lire_data("puzzle")

    # Position actuelle
    pos_actuel = [0, 0]

    # Mouvement
    ls_pos_maisons = []
    for direction in str_directions:
        if direction == "^":
            pos_actuel[1] += 1
        elif direction == "v":
            pos_actuel[1] -= 1
        elif direction == ">":
            pos_actuel[0] += 1
        elif direction == "<":
            pos_actuel[0] -= 1

        # Ajouter la nouvelle position à la liste
        ls_pos_maisons.append((pos_actuel[0], pos_actuel[1]))

    # Calculer le nombre de maisons uniques visitées
    nb_maisons = len(set(ls_pos_maisons))

    return nb_maisons


if __name__ == "__main__":
    print(do_solution_1())
