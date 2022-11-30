def fn_lire_data(nom_data: str) -> int:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        str_input = puzzle_input.read()

    # Longueur totale
    espace_inital = len(str_input.replace("\n", ""))

    # Combien il y a de \", on va ajouter 2 au total pour chaque occurrence
    ajouter_bs_guill = str_input.count(r'\"') * 2

    # Combien il y a de \\, on va ajouter 2 au total pour chaque occurrence
    ajouter_bs_bs = str_input.count(r'\\') * 1

    # Combien il y a de \x, on va ajouter 1 au total pour chaque occurrence
    ajouter_bs_x = str_input.count(r'\x')

    # Combien il y a de lignes, on ajoute 4 par ligne à cause des "" de début et fin
    ajouter_lignes = len([ligne for ligne in str_input.split("\n")]) * 4

    return ajouter_lignes + ajouter_bs_guill + ajouter_bs_x + ajouter_bs_bs


def do_solution_1() -> int:
    reponse = fn_lire_data("puzzle")
    return reponse


if __name__ == "__main__":
    print(do_solution_1())
