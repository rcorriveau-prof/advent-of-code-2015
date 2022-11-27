def fn_lire_data(nom_data: str) -> str:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        return puzzle_input.read()


def do_solution_1() -> int:
    puzzle_data = fn_lire_data("puzzle")

    etage = 0
    for parenthese in puzzle_data:
        if parenthese == "(":
            etage += 1
        else:
            etage -= 1
    return etage


if __name__ == "__main__":
    print(do_solution_1())
