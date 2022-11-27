from typing import List


def fn_lire_data(nom_data: str) -> List[str]:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return [ligne.strip() for ligne in puzzle_input.readlines()]


def fn_prep_data(p_puzzle_data: any) -> any:
    ls_cadeaux = [ligne.split("x") for ligne in p_puzzle_data]
    ls_cadeaux_int = [list(map(int, cadeau)) for cadeau in ls_cadeaux]  # Convertir les str en int
    return ls_cadeaux_int  # Liste de liste, chacune contient 3 chiffres


def do_solution_1() -> int:
    puzzle_data = fn_lire_data("puzzle")
    ls_cadeaux = fn_prep_data(puzzle_data)

    total_pied_carre_papier = 0
    for cadeau in ls_cadeaux:
        # Liste des 3 superficie
        ls_cotes = (cadeau[0] * cadeau[1]), (cadeau[0] * cadeau[2]), (cadeau[1] * cadeau[2])
        # Ajoute le plus petit coté
        total_pied_carre_papier += min(ls_cotes)
        # Ajoute tous les cotes, 2 fois
        total_pied_carre_papier += sum(ls_cotes) * 2

    return total_pied_carre_papier


if __name__ == "__main__":
    print(do_solution_1())
