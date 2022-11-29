import numpy as np


def fn_lire_data(nom_data: str) -> str:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read()


def fn_prep_data(p_puzzle_data: any) -> any:
    p_puzzle_data = p_puzzle_data.replace("turn ", "")
    p_puzzle_data = p_puzzle_data.replace("through ", "")
    ls_actions = []
    for ligne in p_puzzle_data.split("\n"):
        ls_ligne = ligne.split(" ")
        action = ls_ligne[0]
        coords_1 = tuple(map(int, ls_ligne[1].split(",")))
        coords_2 = tuple(map(int, ls_ligne[2].split(",")))
        ls_actions.append((action, coords_1, coords_2))
    return tuple(ls_actions)


def do_solution_1() -> int:
    puzzle_data = fn_lire_data("puzzle")
    tp_actions = fn_prep_data(puzzle_data)

    # Créer le tableau avec numpy
    array_2d = np.zeros((1000, 1000))
    for actions, coord1, coord2 in tp_actions:
        for rangee in range(coord1[1], coord2[1] + 1):
                for colonne in range(coord1[0], coord2[0] + 1):
                    if actions == "on":  # Mets à 1
                        array_2d[colonne][rangee] = 1
                    elif actions == "off":  # Mets à 0
                        array_2d[colonne][rangee] = 0
                    else:  # Change l'état : 0 -> 1, 1 -> 0
                        if array_2d[colonne][rangee] == 1:
                            array_2d[colonne][rangee] = 0
                        else:
                            array_2d[colonne][rangee] = 1

    # Compter les "1", lumières allumées
    return np.count_nonzero(array_2d)


if __name__ == "__main__":
    print(do_solution_1())

    # test réponse : 998996