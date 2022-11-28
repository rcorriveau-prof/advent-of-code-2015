import hashlib
import re


def fn_lire_data(nom_data: str) -> str:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read().strip("\n")


def do_solution_1():
    moitie_lettre = fn_lire_data("puzzle")
    moitie_chiffre = 1
    while True:
        full_texte = moitie_lettre + str(moitie_chiffre)
        resultat = hashlib.md5(full_texte.encode())

        if re.match(r"^00000\d", resultat.hexdigest()):
            break
        else:
            moitie_chiffre += 1

    return moitie_chiffre


if __name__ == "__main__":
    print(do_solution_1())
    # Réponse test : 609043
