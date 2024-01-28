atoms = {
#   'ELEMENT' = (name, atomic mass)
#   change to json?
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

orbital_capacity = {
    "s": 2,
    "p": 6,
    "d": 10,
    "f": 14,
}

orbital_order = ("1s", "2s", "2p", "3s", "3p", "4s", "3d",
                 "4p", "5s", "4d", "5p", "6s", "4f", "5d",
                 "6p", "7s", "5f", "6d", "7p")

class Atom:
    def __init__(self, element) -> None:
        self.element = element
        self.element_name, self.atomic_mass = atoms[element] #tuple unpack
        self.avg_atomic_mass = round(self.atomic_mass, 0)
        self.atomic_number = list(atoms.keys()).index(self.element) + 1

        self.protons = self.atomic_number
        self.neutrons = int(self.avg_atomic_mass - self.protons)
        self.electrons = self.protons
        
        self.period = self.get_period()
        
        self.configuration = self.get_electron_configuration()
    
    def get_period(self) -> int:
        if self.atomic_number >= 1 and self.atomic_number <= 2:
            period = 1
        elif self.atomic_number >= 3 and self.atomic_number <= 10:
            period = 2
        elif self.atomic_number >= 11 and self.atomic_number <= 18:
            period = 3
        elif self.atomic_number >= 19 and self.atomic_number <= 36:
            period = 4
        elif self.atomic_number >= 37 and self.atomic_number <= 54:
            period = 5
        elif self.atomic_number >= 55 and self.atomic_number <= 86:
            period = 6
        elif self.atomic_number >= 87 and self.atomic_number <= 118:
            period = 7
        return period
    
    def get_group(self) -> int:
        last_electron = self.configuration[-1]
        
    
    def get_electron_configuration(self) -> str: #refactor this its really bad
        configuration = ""
        total_electrons = self.electrons
        for orbit in orbital_order:
            orbit_letter = orbit[1]
            orbit_electrons = 0
            for i in range(orbital_capacity[orbit_letter]):
                orbit_electrons += 1
                if total_electrons - orbit_electrons <= 0:
                    break
            configuration += orbit + '^' + str(orbit_electrons) + " "
            
            total_electrons -= orbit_electrons
            if total_electrons <= 0:
                break
        
        return configuration
    
    def display_atom_data(self) -> None:
        print(f"{self.element}: {self.element_name}")
        print(f"[Period: {self.period} Group: N/A Category: N/A]")
        print(f"Avg atomic mass: {self.avg_atomic_mass}u")
        print(f"P: {self.protons}, N: {self.neutrons}, E: {self.electrons}\n")
    
    def display_bohr(self) -> None:
        pass
