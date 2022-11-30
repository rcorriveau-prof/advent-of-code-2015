def fn_lire_data(nom_data: str) -> list:
    with open(f"{nom_data}_input.txt", "r") as puzzle_input:
        str_input = puzzle_input.read()
        str_input = str_input.replace(" ->", "").replace("AND", "&").replace("OR", "|").replace("LSHIFT", "<<").replace(
            "RSHIFT", ">>").replace("NOT", "~")

        return [ligne.strip().split() for ligne in str_input.splitlines()]


def do_solution_1() -> int:
    puzzle_data = fn_lire_data("puzzle")

    # Transformer les nombres en int
    for i, gate in enumerate(puzzle_data):
        for ii, wire in enumerate(gate):
            if wire.isdigit():
                puzzle_data[i][ii] = int(wire)

    #  Reverse engineer, on commence par la fin
    fil_chercher = "a"
    ls_fil_chercher = [fil_chercher]
    sequence_gates = []
    while True:
        sequence_gates.append([gate for gate in puzzle_data if gate[-1] in ls_fil_chercher])

        if not sequence_gates[-1]:  # Rien n'a été trouvé, on ne peut plus remonter, c'est le début
            break

        # Nouveaux fils à chercher
        ls_fil_chercher = []
        for gate in sequence_gates[-1]:  # Dernière gates ajoutées
            for wire in gate[:-1]:  # Le dernier est exclu, on l'a déjà cherché
                if not isinstance(wire, int) and wire not in ["|", "&", "~", "<<", ">>"]:
                    ls_fil_chercher.append(wire)

    sequence_gates.remove([])  # On enlève la dernière entrée vide
    sequence_gates.reverse()  # Inverser la séquence, on remet dans l'ordre

    # On fait le chemin à l'endroit
    wires = {}
    for etapes in sequence_gates:
        for gate in etapes:
            longueur_gate = len(gate)
            if longueur_gate == 2:  # Assignation directe
                valeur, cible = gate
                if isinstance(valeur, int):
                    wires[cible] = valeur
                else:
                    wires[cible] = wires[valeur]
            elif longueur_gate == 3:  # NOT
                operateur, valeur, cible = gate
                if isinstance(valeur, int):
                    wires[cible] = 65535 - valeur
                else:
                    wires[cible] = 65535 - wires[valeur]
            elif longueur_gate == 4:  # AND, OR, LSHIFT, RSHIFT
                valeur1, operateur, valeur2, cible = gate
                if isinstance(valeur1, int) and isinstance(valeur2, int):
                    wires[cible] = eval(f"{valeur1} {operateur} {valeur2}")
                elif isinstance(valeur1, int):
                    wires[cible] = eval(f"{valeur1} {operateur} {wires[valeur2]}")
                elif isinstance(valeur2, int):
                    wires[cible] = eval(f"{wires[valeur1]} {operateur} {valeur2}")
                else:
                    wires[cible] = eval(f"{wires[valeur1]} {operateur} {wires[valeur2]}")



    print(wires)
    return wires[fil_chercher]


if __name__ == "__main__":
    print(do_solution_1())
