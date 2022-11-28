def fn_lire_data(nom_data: str) -> str:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read()


def bouger_perso(position_actuelle: list, direction: str) -> list:
    if direction == "^":
        position_actuelle[1] += 1
    elif direction == "v":
        position_actuelle[1] -= 1
    elif direction == ">":
        position_actuelle[0] += 1
    elif direction == "<":
        position_actuelle[0] -= 1

    return position_actuelle


def do_solution_2() -> int:
    str_directions = fn_lire_data("puzzle")

    # Position actuelle
    pos_actuel_santa = [0, 0]
    pos_actuel_robot = [0, 0]

    # Mouvement
    ls_pos_maisons = []
    tour_santa = True
    for direction in str_directions:
        if tour_santa:
            pos_actuel_santa = bouger_perso(pos_actuel_santa, direction)
            # Ajouter la nouvelle position à la liste
            ls_pos_maisons.append((pos_actuel_santa[0], pos_actuel_santa[1]))
            tour_santa = False
        else:
            pos_actuel_robot = bouger_perso(pos_actuel_robot, direction)
            # Ajouter la nouvelle position à la liste
            ls_pos_maisons.append((pos_actuel_robot[0], pos_actuel_robot[1]))
            tour_santa = True

    # Calculer le nombre de maisons uniques visitées
    nb_maisons = len(set(ls_pos_maisons))

    return nb_maisons


if __name__ == "__main__":
    print(do_solution_2())
