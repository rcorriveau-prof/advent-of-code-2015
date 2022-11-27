def fn_lire_data(nom_data: str) -> str:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read()


def do_solution_2() -> int:
    puzzle_data = fn_lire_data("puzzle")

    etage = 0
    for position, parenthese in enumerate(puzzle_data):
        if parenthese == "(":  # Bouger selon les étages
            etage += 1
        else:
            etage -= 1
        if etage == -1:  # Entre dans le le sous-sol
            return position + 1  # L'index commence à zéro, mais pas le document.


if __name__ == "__main__":
    print(do_solution_2())
