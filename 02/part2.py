from typing import List
from math import prod


def fn_lire_data(nom_data: str) -> List[str]:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return [ligne.strip() for ligne in puzzle_input.readlines()]


def fn_prep_data(p_puzzle_data: any) -> any:
    ls_cadeaux = [ligne.split("x") for ligne in p_puzzle_data]
    ls_cadeaux_int = [list(map(int, cadeau)) for cadeau in ls_cadeaux]  # Convertir les str en int
    return ls_cadeaux_int  # Liste de liste, chacune contient 3 chiffres


def do_solution_2() -> int:
    puzzle_data = fn_lire_data("puzzle")
    ls_cadeaux = fn_prep_data(puzzle_data)

    total_pied_ruban = 0
    for cadeau in ls_cadeaux:
        # Ajoute le volume en pieds de ruban
        total_pied_ruban += prod(cadeau)
        # Enlève le plus grand coté
        cadeau.remove(max(cadeau))
        # Ajoute la longueur des cotés, 2 fois
        total_pied_ruban += sum(cadeau) * 2

    return total_pied_ruban


if __name__ == "__main__":
    print(do_solution_2())
