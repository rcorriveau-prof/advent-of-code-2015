def fn_lire_data(nom_data: str) -> int:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        str_input = puzzle_input.read()

    # Longueur totale
    espace_inital = len(str_input.replace("\n", ""))

    # Nb lignes, plus 4 pour chaque ligne à cause des "" de début et fin
    nb_ligne = len([ligne for ligne in str_input.split("\n")])

    # Combien il y a de " en milieu de ligne, ils comptent pour 1
    nb_guill = str_input.count(r'"')
    nb_guill = nb_guill - (nb_ligne * 2)

    # Combien il y a de \, on ajoute 1 pour chacun
    nb_bs = str_input.count('\\')

    return nb_bs + nb_guill + (nb_ligne * 4)


def do_solution_1() -> int:
    reponse = fn_lire_data("puzzle")
    return reponse


if __name__ == "__main__":
    print(do_solution_1())
