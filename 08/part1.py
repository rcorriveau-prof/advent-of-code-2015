import re


def fn_lire_data(nom_data: str) -> int:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        str_input = puzzle_input.read()

    # Longueur totale
    espace_total = len(str_input.replace("\n", ""))

    # On enlève les \\ et les \"
    str_input = str_input.replace(r"\\", "1").replace(r"\"", "1")

    # On enlève les \x00
    str_input = re.sub(r"\\x..", "1", str_input)
    ls_input = [ligne.strip("\"") for ligne in str_input.split("\n")]

    # Longueur des caractères en mémoire
    espace_memoire = len("".join(ls_input))

    return espace_total - espace_memoire


def do_solution_1() -> int:
    reponse = fn_lire_data("puzzle")
    return reponse


if __name__ == "__main__":
    print(do_solution_1())
