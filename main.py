import math

atoms = {
#   'ELEMENT' = (name, atomic mass)
    'H': ("Hydrogen", 1.0078),
    'He': ("Helium", 4.0026),
    'Li': ("Lithium", 6.9410),
    'Be': ("Beryllium", 9.0122),
    'B': ("Boron", 10.811),
    'C': ("Carbon", 12.011),
    'N': ("Nitrogen", 14.007),
    'O': ("Oxygen", 15.999),
    'F': ("Fluorine", 18.998),
    'Ne': ("Neon", 20.180),
    'Na': ("Sodium", 22.990),
    'Mg': ("Magnesium", 24.305),
    'Al': ("Aluminum", 26.982),
    'Si': ("Silicon", 28.086),
    'P': ("Phosphorus", 30.974),
    'S': ("Sulfur", 32.065),
    'Cl': ("Chlorine", 35.453),
    'Ar': ("Argon", 39.948),
    'K': ("Potassium", 39.098),
    'Ca': ("Calcium", 40.078),
    'Sc': ("Scandium", 44.956),
    'Ti': ("Titanium", 47.867),
    'V': ("Vanadium", 50.942),
    'Cr': ("Chromium", 51.996),
    'Mn': ("Manganese", 54.938),
    'Fe': ("Iron", 55.845),
    'Co': ("Cobalt", 58.933),
    'Ni': ("Nickel", 58.693),
    'Cu': ("Copper", 63.546),
    'Zn': ("Zinc", 65.380),
    'Ga': ("Gallium", 69.723),
    'Ge': ("Germanium", 72.640),
    'As': ("Arsenic", 74.922),
    'Se': ("Selenium", 78.960),
    'Br': ("Bromine", 79.904),
    'Kr': ("Krypton", 83.798),
    'Rb': ("Rubidium", 85.468),
    'Sr': ("Strontium", 87.620),
    'Y': ("Yttrium", 88.906),
    'Zr': ("Zirconium", 91.224),
    'Nb': ("Niobium", 92.906),
    'Mo': ("Molybdenum", 95.950),
    'Tc': ("Technetium", 98),
    'Ru': ("Ruthenium", 101.07),
    'Rh': ("Rhodium", 102.91),
    'Pd': ("Palladium", 106.42),
    'Ag': ("Silver", 107.87),
    'Cd': ("Cadmium", 112.41),
    'In': ("Indium", 114.82),
    'Sn': ("Tin", 118.71),
    'Sb': ("Antimony", 121.76),
    'Te': ("Tellurium", 127.60),
    'I': ("Iodine", 126.90),
    'Xe': ("Xenon", 131.29),
}

def get_period(atomic_num) -> int:
    period = -1
    if atomic_num >= 1 and atomic_num <= 2:
        period = 1
    elif atomic_num >= 3 and atomic_num <= 10:
        period = 2
    elif atomic_num >= 11 and atomic_num <= 18:
        period = 3
    elif atomic_num >= 19 and atomic_num <= 36:
        period = 4
    elif atomic_num >= 37 and atomic_num <= 54:
        period = 5
    elif atomic_num >= 55 and atomic_num <= 86:
        period = 6
    elif atomic_num >= 87 and atomic_num <= 118: #debatable?
        period = 7
    return period

def get_group(atomic_num, period) -> int:
    pass

def get_atomic_data(element, atomic_num) -> tuple:
    name, atomic_mass = atoms[element]
    avg_atomic_mass = round(atomic_mass, 0)
    
    protons = float(atomic_num)
    
    neutrons = avg_atomic_mass - protons
    electrons = protons
    
    period = get_period(atomic_num)
    print(f"{element}: {name}\n[Period: {period} Group: N/A Category: N/A]")
    print(f"Avg atomic mass: {avg_atomic_mass}u")
    print(f"P: {protons}, N: {neutrons}, E: {electrons}\n")
    
    # perioid/column, type, quantum numbers, bohr model

def choose_element_loop():
    while True:
        inp = input("\nEnter an element symbol, name, atomic #, or X to exit:\n").capitalize()

        if inp == 'X':
            print("\n---------------------------")
            break
        elif inp in atoms:
            get_atomic_data(inp, list(atoms.keys()).index(inp) + 1)
            continue
        else:
            found = False
            for index, key in enumerate(atoms):
                if atoms[key][0] == inp:
                    get_atomic_data(key, index + 1)
                    found = True
                    break
            if found: continue
        try:
            atom = list(atoms)[int(inp) - 1]
            get_atomic_data(atom, int(inp))
        except (ValueError, IndexError) as error:
            print("Bad input, try again.\n")
            continue

def list_all_elements():
    for i, key in enumerate(atoms):
        get_atomic_data(key, i + 1)

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
    
    #for i, key in enumerate(atoms): # do input instead. * for all elements, ext to stop.
    #    get_atomic_data(key, i + 1)

if __name__ == "__main__":
    main()
