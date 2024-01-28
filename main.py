import math
from atom import atoms, Atom

def choose_element_loop():
    while True:
        inp = input("\nEnter an element symbol, name, atomic #, or X to exit:\n").capitalize()
        new_atom = None
        
        if inp == 'X':
            print("\n---------------------------")
            break
        elif inp in atoms:
            new_atom = Atom(inp)
        else:
            for _, key in enumerate(atoms):
                if atoms[key][0] == inp:
                    new_atom = Atom(key)
                    break
        if new_atom == None:
            try:
                new_atom = Atom(list(atoms)[int(inp) - 1])
            except (ValueError, IndexError):
                print("Bad input, try again.\n")
                continue
        
        new_atom.display_atom_data()

def list_all_elements():
    for _, key in enumerate(atoms):
        new_atom = Atom(key)
        new_atom.display_atom_data()

def main():
    while True:
        try:
            inp = input("Would you like to (1) list all elements, (2) choose them, or (X) to exit?\n")
            if inp == 'x' or inp == 'X':
                print("\n---------------------------")
                break
            if int(inp) == 1:
                list_all_elements()
            elif int(inp) == 2:
                choose_element_loop()
            else:
                raise ValueError("Bad input.")
        except ValueError:
            print("Invalid input, try again.\n")

if __name__ == "__main__":
    main()
