from itertools import permutations


def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return [ligne.strip() for ligne in puzzle_input.readlines()]


def fn_prep_data(p_puzzle_data: any) -> any:
    dt_trajets = {}
    for trajet in p_puzzle_data:
        ville1, _, ville2, _, distance = trajet.split()
        # Création des clés de dictionnaires
        if ville1 not in dt_trajets.keys():
            dt_trajets[ville1] = {}
        if ville2 not in dt_trajets.keys():
            dt_trajets[ville2] = {}
        dt_trajets[ville1][ville2] = int(distance)
        dt_trajets[ville2][ville1] = int(distance)
    return dt_trajets


def do_solution_1() -> int:
    puzzle_data = fn_lire_data("puzzle")
    dt_trajets = fn_prep_data(puzzle_data)

    # Créer toutes les permutations
    ls_trajets = permutations(dt_trajets.keys())

    # Calculer toutes les distances
    ls_distances_possibles = []
    for trajet in ls_trajets:
        distance_total = 0
        for position, ville in enumerate(trajet):
            if position == len(trajet) - 1:  # Dernière position, pas de suivant
                break
            distance_total += dt_trajets[ville][trajet[position + 1]]
        ls_distances_possibles.append(distance_total)

    # La plus petite valeur
    return min(ls_distances_possibles)


if __name__ == "__main__":
    print(do_solution_1())
